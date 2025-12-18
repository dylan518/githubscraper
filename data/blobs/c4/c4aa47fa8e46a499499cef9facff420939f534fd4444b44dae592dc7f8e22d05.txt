package com.dobleadev.moneyconverter.services;

import com.dobleadev.moneyconverter.helpers.ConsoleHelper;
import com.dobleadev.moneyconverter.helpers.HttpHelper;
import com.dobleadev.moneyconverter.modules.Currency;
import com.dobleadev.moneyconverter.modules.CurrencyExchangeRateApiList;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.GsonBuilder;

import javax.swing.text.DateFormatter;
import java.time.LocalDateTime;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeFormatterBuilder;
import java.util.List;
import java.util.Scanner;

public class CurrencyExchangeService {
    Gson gson = new GsonBuilder()
            .create();
    String defaultCurrency = "USD";
    Currency fromCurrency = new Currency(defaultCurrency, "US");
    Currency toCurrency = new Currency(defaultCurrency, "US");
    ConversionSaveService conversionSaveService = new ConversionSaveService();

    public Currency getFromCurrency() {
        return fromCurrency;
    }

    public Currency getToCurrency() {
        return toCurrency;
    }

    public void setFromCurrency(Currency fromCurrency) {
        this.fromCurrency = fromCurrency;
    }

    public void setToCurrency(Currency toCurrency) {
        this.toCurrency = toCurrency;
    }

    public void doExchange() {
        try {
            System.out.print("Cuantos $" + fromCurrency + " quieres convertir a " + toCurrency + "?\nCantidad: ");
            double quantity = ConsoleHelper.getInput().nextDouble();
            
            String jsonResponse = HttpHelper.requestData("https://v6.exchangerate-api.com/v6/96ae7394859d92c682c56188/latest/" + fromCurrency);
            JsonObject response = gson.fromJson(jsonResponse, JsonObject.class);
            JsonObject conversionRates = response.getAsJsonObject("conversion_rates");

            if (conversionRates.has(toCurrency.getType())) {
                Double conversionRate = conversionRates.get(toCurrency.getType()).getAsDouble();
//                System.out.println("Conversion rate for " + toCurrency + ": " + conversionRate);
                String result = fromCurrency + "$" + quantity + " = " + toCurrency + "$" + (conversionRate * quantity);
                System.out.println("RESULTADO: " + result);

                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
                String dateTimeFormatter = LocalDateTime.now().format(formatter);
                conversionSaveService.askToSave("[" + dateTimeFormatter + "] " + result);
            } else {
                System.out.println("Currency code not found: " + toCurrency);
                ConsoleHelper.waitForInput();
            }
        } catch (Exception e) {
            System.out.println("ERROR: " + e.getMessage());
            ConsoleHelper.waitForInput();
        }
    }

    public Currency changeExchangeType(Currency currency) {
        try {
            while (true)
            {
                System.out.println("Elije el peso a cambiar: ");
                List<String[]> supportedCodes = gson.fromJson(HttpHelper.requestData("https://v6.exchangerate-api.com/v6/96ae7394859d92c682c56188/codes"), CurrencyExchangeRateApiList.class).supported_codes();
                for (String[] item: supportedCodes) {
                    System.out.print("[" + item[0] + "]");
                }
                System.out.print("\nDigite su eleccion: ");
                String currencyChoice = ConsoleHelper.getInput().nextLine();
                String[] currencyFounded = null;

                for (String[] item: supportedCodes) {
                    if (item[0].equals(currencyChoice)) {
                        currencyFounded = item;
                        break;
                    }
                }

                if (currencyFounded != null) {
                    System.out.println("Se encontró a " + currencyChoice);
                    return new Currency(currencyFounded[0], "");
                } else {
                    System.out.println("ERROR - No se encontró el peso ingresado.");
                    ConsoleHelper.waitForInput();
                }
            }
        } catch (Exception e) {
//            throw new RuntimeException();
            System.out.println("Error inesperado:\n" + e.getMessage());
            ConsoleHelper.waitForInput();
        }
        return currency;
    }
}

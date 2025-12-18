package br.com.alura.conversormoeda.main;

import br.com.alura.conversormoeda.classes.Conversion;
import br.com.alura.conversormoeda.classes.Menu;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        Scanner read = new Scanner(System.in);
        Scanner value = new Scanner(System.in);
        String option = "";
        double readValue = 0;

        while(!option.equals("0")) {
           new Menu();
            option = read.nextLine();

            switch (option){
                case "1":
                    System.out.println("Digite o valor a ser convertido: ");
                     readValue = value.nextDouble();
                    Conversion.getConvertValue("USD", "BRL", readValue);
                    break;
                case "2":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("BRL", "USD", readValue);
                    break;
                case "3":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("EUR", "BRL", readValue);
                    break;
                case "4":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("BRL", "EUR", readValue);
                    break;
                case "5":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("GBP", "BRL", readValue);
                    break;
                case "6":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("BRL", "GBP", readValue);
                    break;
                case "7":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("USD", "EUR", readValue);
                    break;
                case "8":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("EUR", "USD", readValue);
                    break;
                case "9":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("USD", "GBP", readValue);
                    break;
                case "10":
                    System.out.println("Digite o valor a ser convertido: ");
                    readValue = value.nextDouble();
                    Conversion.getConvertValue("GBP", "USD", readValue);
                    break;
                case "0":
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Escolha umas opções válidas!");
                    break;
            }
        }
        read.close();
        value.close();
    }
}

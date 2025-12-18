package com.company;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.text.DecimalFormat;

public class Currency_Exchange {
    private JButton Convert_Button;
    private JTextField philippinesPesoTextField;
    private JTextField otherCurrenciesTextField;
    private JPanel Currency;
    private JLabel Currency_Converter;
    private JLabel To;
    private JLabel From;

    double Usd, Php, Hkd, Mxp, Bp, Cy, Eur;

    String CurrencyOutputStr;
    String PhpStr;


    public Currency_Exchange() {
        DecimalFormat decimal = new DecimalFormat("0.00");
        Convert_Button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                PhpStr = JOptionPane.showInputDialog("Enter Amount to be converted in Philippines Pesos:");
                Php = Double.parseDouble(PhpStr);

                Usd = Php / 50.61;
                Hkd = Php / 6.52;
                Mxp = Php / 2.72;
                Bp = Php / 4.61;
                Cy = Php / 7.24;
                Eur = Php / 54.85;

                CurrencyOutputStr = "\nPhilippines Peso: " + decimal.format(Php) +
                        "\nUS Dollar: " + decimal.format(Usd) +
                        "\nHongKong Dollar: " + decimal.format(Hkd) +
                        "\nBotswana Pula: " + decimal.format(Bp) +
                        "\nMexican Peso: " + decimal.format(Mxp) +
                        "\nEuro: " + decimal.format(Eur) +
                        "\nChinese Yuan: " + decimal.format(Cy);
                JOptionPane.showMessageDialog(null,CurrencyOutputStr);
                System.exit(0);
            }
        });

    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Currency Test 1");
        frame.setContentPane(new Currency_Exchange().Currency);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
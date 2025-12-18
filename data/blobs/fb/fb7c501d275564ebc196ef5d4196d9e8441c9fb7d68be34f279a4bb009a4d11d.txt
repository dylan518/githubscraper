package com.learn.input_output;

import java.util.Scanner;

// Program to convert temperature from Centigrade to Fahrenheit
public class Q12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input temperature in Centigrade
        System.out.print("Enter the temperature in Centigrade (°C): ");
        double tempCentigrade = sc.nextDouble();

        // Convert to Fahrenheit
        double tempFahrenheit = (tempCentigrade * 1.8) + 32;

        // Display the result
        System.out.printf("The equivalent temperature in Fahrenheit is: %.2f°F%n", tempFahrenheit);
    }
}

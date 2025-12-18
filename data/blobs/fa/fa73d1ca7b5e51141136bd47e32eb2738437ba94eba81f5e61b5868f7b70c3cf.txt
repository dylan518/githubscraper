package exercises;

import java.util.Scanner;

/**
 * (Financial application: calculate tips) Write a program that reads the subtotal
 * and the gratuity rate and then computes the gratuity and total. For example, if the
 * user enters 10 for subtotal and 12% for gratuity rate, the program displays $1.2
 * as gratuity and $11.2 as total.
 */
public class Exercise5 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the subtotal and a gratuity rate: ");
        double subTotal = scanner.nextDouble();
        double gratuityRate = scanner.nextDouble();

        double calculateGratuity = subTotal * (gratuityRate / 100);
        double calculateTotal = subTotal + calculateGratuity;

        System.out.println("The gratuity is: " + calculateGratuity + " and total is " + calculateTotal);
    }
}

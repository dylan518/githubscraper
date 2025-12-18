package javaprograms;

import java.util.Scanner;

/**
 * Write a java program to input any two number and ask user to enter their symbol (+, -, /, *)
 * find addition, Subtraction, multiplication and division according to their symbol (using if else)
 */

public class InputNumberAndSymbol_10 {

    public static void main(String[] args) {
        // declare scanner
        Scanner scanner = new Scanner(System.in);

        //input two number
        System.out.println("Enter the first number: ");
        double num1 = scanner.nextDouble();

        System.out.println("Enter second number: ");
        double num2 = scanner.nextDouble();

        //input operation symbol
        System.out.println("Enter the operation symbol(+,-, /, * ): ");
        char operation = scanner.next().charAt(0);

        // directly calling calculate method into main method
        calculate(num1, num2, operation);

        //close scanner
        scanner.close();
    }

    //create method
    public static void calculate(double num1, double num2, char operation) {
        double result;

        if (operation == '+') {
            result = num1 + num2;
            System.out.println("Result: " + num1 + " + " + num2 + " = " + result);
        } else if (operation == '-') {
            result = num1 - num2;
            System.out.println("Result: " + num1 + " - " + num2 + " = " + result);
        } else if (operation == '*') {
            result = num1 * num2;
            System.out.println("Result: " + num1 + " * " + num2 + " = " + result);
        } else if (operation == '/') {
            if (num2 != 0) {// check for division by zero
            } else {
                System.out.println("Error: Division by zero is not allowed.");
            }
            result = num1 / num2;
            System.out.println("Result: " + num1 + " / " + num2 + " = " + result);
        } else {
            System.out.println("Invalid operation symbol.");
        }
    }
}

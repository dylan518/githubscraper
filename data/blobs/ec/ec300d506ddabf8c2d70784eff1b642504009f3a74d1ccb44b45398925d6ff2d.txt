package com.company;

import java.util.Scanner;

public class Exercise18 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Input an integer(positive/negative):");
        int numInt;
        numInt = scanner.nextInt();
        System.out.println("The first digit : " + firstDigit(numInt));
    }

    public static int firstDigit(int num) {
        num = Math.abs(num);
        String number = Integer.toString(num);
        return Integer.parseInt(String.valueOf(number.charAt(0)));
    }
}

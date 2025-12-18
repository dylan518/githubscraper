package Aleksandar.Week1;

import java.util.Scanner;

public class Task3_Finra {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Enter a number:");

        int num = input.nextInt();

        while (!(num % 3 == 0 || num % 5 ==0)){
            System.out.println("Please, enter your number again");
            num = input.nextInt();
        }

            if (num > 0 && num <= 30) {

                if (num % 3 == 0 && num % 5 == 0) {
                    System.out.println("FINRA");
                } else if (num % 5 == 0) {
                    System.out.println("RA");
                } else if (num % 3 == 0) {
                    System.out.println("FIN");
                } else {
                    System.out.println("Invalid number");
                }
            } else {
                System.out.println("Number is out of range");
            }

            input.close();

    }

}
/*
 Numbers -- FINRA
Write a method that prints out the numbers from 1 to 30 but;
for numbers which are multiple of 3 print "FIN" instead of the number,
for numbers which are multiple of 5, print "RA" instead of the number,
and for numbers which are multiple of both 3 and 5, print "FINRA" instead of the number.
 */

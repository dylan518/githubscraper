package day03;

import java.util.Scanner;

public class P08_WhileLoop {
    public static void main(String[] args) {
        //write a java code which will ask user to enter number more than 2 digits
        //and check if the number is palindrome

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a natural number more than 2 digits");
        int originalInput = scanner.nextInt(); //134

        int reversed = 0;
        int number = originalInput;
        while(number!=0){
            //to get
            int lastDigit = number%10; //to get last digit
            reversed = reversed *10 + lastDigit; //to write given number in reverse
            number = number/10; //to remove last digit

        }
        System.out.println("reversed: "+reversed);
        if(reversed==originalInput){
            System.out.println("The number is palindrome");
        }else{
            System.out.println("The number is not palindrome");
        }
    }
}

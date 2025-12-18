package PracticeJava;

import java.util.Scanner;

public class Task02 {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        System.out.println("Please enter a word");
        String word = scan.next();
        char [] stringCharArray = word.toCharArray();
        String reverse = "";

        for(int i = stringCharArray.length-1; i>=0; i--) {
            reverse = reverse + stringCharArray[i];
        }

        System.out.println(reverse);
    }
    }



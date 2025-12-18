package org.example;

import java.util.Scanner;

public class Pallindrome {

    public static void main(String[] args) {

        int n, sum=0, rev=0;

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        n = sc.nextInt();

        int temp = n;
        while(n>0){
            rev = n%10;
            sum = (sum*10)+rev;
            n = n/10;
        }

        if (sum == temp) {

            System.out.println("pallindrome");
        }
        else{
            System.out.println("not pallindrome");
        }


    }

}

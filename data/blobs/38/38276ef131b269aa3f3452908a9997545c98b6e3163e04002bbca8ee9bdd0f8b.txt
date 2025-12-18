package com.company;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("1. Iphone" +
                "\n"+"2. Samsung" );
        int i;
        Scanner in = new Scanner(System.in);
        i = in.nextInt();
        Select s = new Select();
        switch(i)
        {
            case 1:
                s.iphonesale();
                break;
            case 2:
                s.samsungsale();
                break;
            default:
                System.out.println("Enter the right choice");
        }
    }
}

package src.May22;

import java.util.Scanner;

public class gretestNumber {

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Provide first number");
        int first = sc.nextInt();

        Scanner sc2 = new Scanner(System.in);
        int second = sc.nextInt();

        Scanner sc3 = new Scanner(System.in);
        int third = sc.nextInt();

        if (first>second &&first>third)
        {
            System.out.println(first +" is biggest");
        }
        else if(second >first && second >third)
        {
            System.out.println( second +" is biggest");
        }
        else if (third >second && third >first)
        {
            System.out.println(third +" is the biggest");
        }

        else
            System.out.println("Every number is same");

    }
}

package p02_Verzweigung;

import java.util.Scanner;

public class Alterspruefung {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Gebe dein Alter an: ");
        int age = sc.nextInt();
        if (age < 18) {
            System.out.println("Du bist noch minderjährig!");
        } else {
            System.out.println("Du bist schon volljährig!");
        }
    }
}

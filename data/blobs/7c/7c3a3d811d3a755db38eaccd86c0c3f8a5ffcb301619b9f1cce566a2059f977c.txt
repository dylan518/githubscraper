package day2;

import java.util.Scanner;

public class Task17 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Bir tam sayı giriniz: ");
        int sayi = scanner.nextInt();

        System.out.println("Karesi: " + (sayi * sayi));
        System.out.println("Küpü: " + (sayi * sayi * sayi));

        scanner.close();
    }
}


/*
= Açıklama =
Bir tam sayının karesini ve küpünü hesaplayan bir Java programı yazınız.
Program girdiyi almalı ve çıktı olarak karesini ve küpünü göstermelidir.

= Örnek Girdi =
Bir tam sayı giriniz: 3

= Örnek Çıktı =
Karesi: 9
Küpü: 27
*/
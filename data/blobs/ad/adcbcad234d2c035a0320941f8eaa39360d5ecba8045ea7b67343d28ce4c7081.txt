package EllyTaskssss;

import java.util.Scanner;

public class Task22Odev {
    public static void main(String[] args) {
        /*
     Girilen Stringdeki tüm sesli harfleri saymak için bir Java Methodu yazınız.
    Test Data:
    java is fun
    Beklenen Çıktı:4
     */
        Scanner input=new Scanner(System.in);
        System.out.println("String bir ifade giriniz");
        String str= input.nextLine();
        int sayac=0;
        char s;
        int i;
        for (i=0;i<str.length();i++) {
            s = str.charAt(i);
            if (s == 'a' || s == 'e' || s == 'ı' || s == 'i' || s == 'o' || s == 'ö' || s == 'u' || s == 'ü') {

            }
            System.out.println("sayac = " + sayac + "adet sesli harf vardır");

        }}
}

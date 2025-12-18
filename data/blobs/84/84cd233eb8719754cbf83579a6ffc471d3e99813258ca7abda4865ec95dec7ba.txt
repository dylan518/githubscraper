package algorythm2;

import java.util.Scanner;

public class VücutKitleIndeksi {
    public static void main(String[] args) {
        double kg;
        double boy;
        double indeks;

        Scanner scanner = new Scanner(System.in);
        System.out.println("Kg giriniz");
        kg = scanner.nextDouble();
        System.out.println("Boy giriniz");
        boy = scanner.nextDouble();

        indeks = kg/(boy*boy);
        System.out.println(indeks);
    }
}

package pertemuan7;

import java.util.Scanner;

public class kota {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        String[] kota = new String[3];
        System.out.print("Masukan jumlah data : ");
        int n = input.nextInt();

        for (int i = 0; 1 <= n; i++) {
            System.out.print("masukan data ke=" + (i + 1) + ":");
            kota[i-1] = input.next();
        }

        for (String a : kota) {
            System.out.println(a);
        }
    }
}

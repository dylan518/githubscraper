package day15_overloding_forLoop;

public class C01_Returnmethod {
    public static void main(String[] args) {

        // verilen iki sayiyi carpip
        // sonucu bize donduren bir method olusturun

        int sayi1=10;
        int sayi2 =5;

        int sonuc=carpGetir(sayi1,sayi2);
                // method call  carpGetir methoduna git ve sayi1 ve sayi2 al getir.

        System.out.println("sonuc = " + sonuc);
    }

    public static int carpGetir(int sayi1, int sayi2) {
        System.out.println("illa'da sonu ");
        return sayi1*sayi2;

    }
}

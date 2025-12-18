package Day06_İfstatements;

import java.util.Scanner;

public class C09_İfstatementsödevler {
    public static void main(String[] args) {
    //kullanıcıdan dikdörtgenin kenar uzunluklarını isteyin ve dikdörtgenin kare olup olamadıgını yazdırın

        Scanner scan=new Scanner(System.in);
        System.out.println("lütfen dikdörgenin kenar uzunluklarını giriniz");
        double kenar1= scan.nextDouble();
        double kenar2= scan.nextDouble();

        if (kenar1==kenar2){

            System.out.println("girilen dikdörtgen karedir");
        }else {
            System.out.println("girilen dikdörtgen kare degildir");

        }




    }
}

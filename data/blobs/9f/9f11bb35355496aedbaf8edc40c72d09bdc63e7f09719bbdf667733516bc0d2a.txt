package recap01;

import java.util.Scanner;

public class Q03_BMI {
    public static void main(String[] args) {
        /*
        Kullanıcıdan vucut agirligi ve boyunu isteyin ve BMI (Vucut Kitle Indexi) yazdirin
         */

        Scanner scan=new Scanner(System.in);
        System.out.println("Lutfen vucut agirliginizi giriniz");
        double kilo= scan.nextDouble();

        System.out.println("Lutfen boyunuzu 0.00 seklinde giriniz");
        double boy= scan.nextDouble();

        int BMI= (int) (kilo/(boy*boy));

        System.out.println("BMI : "+ BMI);
    }
}

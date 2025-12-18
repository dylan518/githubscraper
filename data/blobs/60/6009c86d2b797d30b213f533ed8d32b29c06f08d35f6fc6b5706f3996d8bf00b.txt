import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
                System.out.println("billetes 100€");
                float bill_100 = sc.nextFloat();
                System.out.println("billetes 20€");
                float bill_20 = sc.nextFloat();
                System.out.println("billetes 5€");
                float bill_5 = sc.nextFloat();
                System.out.println("monedas 1€");
                float mon_1 = sc.nextFloat();
                float total = 100*bill_100+20*bill_20+5*bill_5+mon_1;
                System.out.println("Total ="+ total);




    }


}
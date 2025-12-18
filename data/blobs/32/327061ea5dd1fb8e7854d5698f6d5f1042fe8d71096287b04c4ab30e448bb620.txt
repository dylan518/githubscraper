package ss1_introduction_java.bai_tap.bai_3;

import java.util.Scanner;

public class Convert {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("input USD:");
        int usd = Integer.parseInt(scanner.nextLine());
        System.out.println("Input exchange rate:");
        double exchange_Rate = Double.parseDouble(scanner.nextLine());
        System.out.println(usd * exchange_Rate);
    }
}

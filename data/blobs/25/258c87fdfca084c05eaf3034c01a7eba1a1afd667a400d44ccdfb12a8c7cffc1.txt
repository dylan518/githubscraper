package secao5.exercicios;

import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        double number = sc.nextDouble();
        String validaty = (number > 0) ? "Positivy" : "Negativy";
        System.out.println(validaty);
        sc.close();
    }
}

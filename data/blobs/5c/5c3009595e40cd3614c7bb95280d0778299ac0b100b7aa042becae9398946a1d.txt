package ex05;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Quantos números vai digitar?: ");
        int n = sc.nextInt();

        double[] nums = new double[n];

        for (int i = 0; i < nums.length; i++) {
            System.out.printf("Digite o %d° número: ", i + 1);
            nums[i] = sc.nextDouble();
        }

        double maior = nums[0];
        int posMaior = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > maior) {
                maior = nums[i];
                posMaior = i;
            }
        }

        System.out.println("Maior valor: " + maior + "\nPosição: " + posMaior);

        sc.close();
    }
}

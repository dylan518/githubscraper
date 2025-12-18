package Lab3;

import java.security.SecureRandom;
import java.util.Arrays;
import java.util.Scanner;

public class lab3_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhập số phần tử của mảng: ");
        int n = scanner.nextInt();
        int Sole =0, Sochan =0;
        int[] intArr = new int[n];
        System.out.println("Nhập các phần tử cho mảng: ");
        for (int i = 0; i < n; i++) {
           System.out.print("Nhập phần tử thứ " + i + ": ");
           intArr[i] = scanner.nextInt();
        }
        for (int i = 0; i < n; i++) {
            if (intArr[i] % 2 == 0) {
                Sochan++;
            } else {
              Sole++;
            }
        }
        System.out.println("Số lượng số nguyên chẵn trong mảng = " + Sochan);
    System.out.println("Số lượng số nguyên lẻ trong mảng = " + Sole);
    }
}

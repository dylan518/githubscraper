//2.18

import java.util.Scanner;

public class EulerNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the value of n: ");
        int n = scanner.nextInt();

        double e = calculateEulerNumber(n);
        System.out.println("Euler's number (e) with n = " + n + " is: " + e);

        scanner.close();
    }

    public static double calculateEulerNumber(int n) {
        double e = 1;
        double factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
            e += 1.0 / factorial;
        }
        return e;
    }
}

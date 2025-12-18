import java.util.Scanner;
public class Factorial {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter number up to 16:");
        int num = scanner.nextInt();
        int factorial = fact(num);
        System.out.println("Factorial is:" + factorial);
    }

    static int fact(int n) {
        int output;
        if (n == 1) {
            return 1;
        }
        output = fact(n - 1) * n;
        return output;
    }
}

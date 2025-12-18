import java.util.Scanner;

public class MaxNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("How many numbers do you want to enter?: ");
        int total = scanner.nextInt();
        int[] numbers = new int[total];

        System.out.println("Enter the numbers...");
        for (int i = 0; i < total; i++) {
            numbers[i] = scanner.nextInt();
        }

        System.out.println("Maximum is: " + max(numbers));
        System.out.println("Minimum is: " + min(numbers));

        scanner.close();
    }

    public static int max(int[] numbers) {
        int res = numbers[0];
        for (int number : numbers) {
            if (number > res) {
                res = number;
            }
        }
        return res;
    }

    public static int min(int[] numbers) {
        int res = numbers[0];
        for (int number : numbers) {
            if (number < res) {
                res = number;
            }
        }
        return res;
    }
}

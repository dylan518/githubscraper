import java.util.Scanner;

public class IsPrime {
    public static boolean isPrime(int num) {
        if (num < 2)
            return false; // 0 and 1 are not prime numbers

        for (int i = 2; i * i <= num; i++) { // Optimized loop till sqrt(num). i * i <= num is a clever way of writing i
                                             // <= Math.sqrt(num) without using the Math class.
            if (num % i == 0) {
                return false; // If num is divisible by i, it's not prime
            }
        }
        return true; // If no divisors found, it's prime
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to check if it's prime: ");
        int num = sc.nextInt();
        sc.close();
        System.out.println(num + " is " + (isPrime(num) ? "a prime number" : "not a prime number"));
    }
}

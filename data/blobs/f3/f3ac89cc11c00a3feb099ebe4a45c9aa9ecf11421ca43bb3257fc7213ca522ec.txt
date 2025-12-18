package codetalksdna.CodingPrograms;

import java.util.Scanner;

public class NumberOfDigits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int count = 0;
        int num = sc.nextInt();
        String value = String.valueOf(num);
        System.out.println(value.length());

        while (num != 0) {
            num = num / 10;
            count++;
        }
        System.out.println(count);
    }
}

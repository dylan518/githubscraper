package day09;
import java.util.Scanner;

public class firstScanner {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("please enter a number");

        int number = input.nextInt();
        System.out.println("this is your number " + number);
    }
}

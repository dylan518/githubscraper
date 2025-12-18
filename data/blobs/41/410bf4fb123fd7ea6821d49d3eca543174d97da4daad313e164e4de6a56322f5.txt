package Reviews;

import java.util.Scanner;

public class CalculateFibonacci {

    public static void main(String[] args) {
        System.out.println("Please enter the number in your Fib Sequence");
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        CalculateFibonacci cf = new CalculateFibonacci();
        cf.printFib(num);

    }

    public void printFib(int num) {
        int first = 1;
        int second = 1;
        if (num <= 0) {
            System.out.println("You must enter a positive number");
        }
        if (num >= 1) {
            System.out.print("1 ");
        }
        if (num >= 2) {
            System.out.print("1 ");
        }
        for (int index = 3; index <= num; index++) {
            System.out.print(first + second + " ");
            int temp = first;  // or int temp = first + second;
            first = second;
             second = temp + second; //second += temp;

        }

    }

}

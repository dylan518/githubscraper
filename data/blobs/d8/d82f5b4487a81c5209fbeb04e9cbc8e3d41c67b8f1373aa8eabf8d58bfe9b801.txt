package SimpleQue;

import java.util.Scanner;

public class FibonacciUsingRecursion {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number");
        int n = sc.nextInt();
        for (int i=1;i<=n;i++) {
            System.out.println(isFibonacci(i));
        }
    }
    public static int isFibonacci(int input){
        if(input==0 || input==1){
            return 1;
        }
        else {
            return isFibonacci(input-1)+ isFibonacci(input-2);
        }

    }
}

package BasicJava;

import java.util.Scanner;

public class PrimeNumberCheck {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter Number");
        int n;
        n = scan.nextInt();
        int count=0;
        for(int i=2;i<n/2;i++)
        {
            for(int j=2;j<i;j++)
            {
                if(i%j==0) count++;
            }
        }
        if(count>1) System.out.println("Not a Prime Number");
        else System.out.println("Prime Number");
    }
}

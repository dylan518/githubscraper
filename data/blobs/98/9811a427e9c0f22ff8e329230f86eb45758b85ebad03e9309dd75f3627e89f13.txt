import java.util.Scanner;
public class Factorial {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number");
        int n=sc.nextInt();
        int fact=1;
        int i=2;
        while(i<=n)
        {
            fact=fact*i;
            i++;
        }
        System.out.println("Factorial of"+n+"is "+fact);
    }
}

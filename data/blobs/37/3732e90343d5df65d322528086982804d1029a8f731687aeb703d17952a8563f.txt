import java.util.Scanner;
public class exception1 {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter str1: ");
        String str1=sc.nextLine();
        System.out.print("Enter str2: ");
        String str2=sc.nextLine();
        try{
            int num1=Integer.parseInt(str1);
            int num2=Integer.parseInt(str2);
            int sum=num1+num2;
            System.out.println("Sum of the two numbers: "+sum);
        }
        catch(NumberFormatException e)
        {
            System.out.println("Can add only numbers");
        }
    }
}

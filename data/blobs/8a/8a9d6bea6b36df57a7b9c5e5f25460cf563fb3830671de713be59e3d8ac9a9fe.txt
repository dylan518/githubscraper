package Exercise98;
import java.util.Scanner;

// Divider cant be 0
public class Ex5
{
    static int num1, num2;
    static Scanner scan = new Scanner(System.in);

    public static void divide(int num1, int num2) throws ArithmeticException
    {
        System.out.println("Num1 / Num2 = " + (num1/num2));
    }

    public static void main(String[] args)
    {
        System.out.print("Enter the first int: ");
        num1 = scan.nextInt();
        System.out.print("Enter the second int: ");
        num2 = scan.nextInt();

        try
        {
            divide(num1, num2);
        }
        catch(ArithmeticException e)
        {
            System.out.println("除数不能为0");
        }
        finally
        {
            scan.close();
        }
    }
}
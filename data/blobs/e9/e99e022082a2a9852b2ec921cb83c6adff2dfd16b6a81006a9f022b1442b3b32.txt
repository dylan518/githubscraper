package NovW3;
//Liner search Arrray;//
import java.util.Scanner;
public class ArrayWithScanner {
    public static void main(String[] args)
    {
        int arr[]={10,12,15,18,20,35,40,15,30,50,60};
        Scanner s=new Scanner(System.in);
        System.out.println("10,12,15,18,20,35,40,15,30,50,60");
        System.out.println("Select the number in list.");
        int no=s.nextInt();
        int number=no;
        int temp=0;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]==number)
            {
                System.out.println(i+". This is index value .");
                temp=temp+1;
        }
        }
if(temp==0)
{
    System.out.println(number+". number is not found in list.");
}

    }
}
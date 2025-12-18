import java.util.*;
public class Third {
    public static void main(String args[])
    {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the size of array");
        int size= sc.nextInt();
        int[] arr= new int[size];

        for(int i=0;i<size;i++)
        {
            System.out.println("Enter the Element of the arry");
            arr[i]= sc.nextInt();
        }
        System.out.println("Array elements are:");
        for(int i=0;i<arr.length;i++)
        {
            
            System.out.print(arr[i]+" ");
        }
    }
}

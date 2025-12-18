// Find the no. of occurrence of each element in a user entered list of nos.

package Class.Lab_Assignment_2;

import java.util.Scanner;

public class ques5 {
    static void occurrence(int arr[],int n)
    {
        for(int i=0;i<n;i++)
        {
            int count=1;
            if(arr[i]==-1)
            {
                continue;
            }
            for(int j=i+1;j<n;j++)
            {
                if(arr[i]==arr[j])
                {
                    arr[j]=-1;
                    count++;
                }
            }
            System.out.println("Occurence of "+arr[i]+" is : "+count+"\n");
        }
    }
    static void display(int arr[],int n)
    {
        for(int i=0;i<n;i++)
        {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n;
        System.out.println("Enter the size of your array ");
        n=sc.nextInt();
        int arr[]=new int[n];
        System.out.println("Enter the array elements ");
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        System.out.println("Displaying your array elements before sorting ");
        display(arr, n);
        occurrence(arr, n);
        sc.close();
    }
}

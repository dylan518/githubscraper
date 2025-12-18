import java.util.*;
class Array
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int n,temp;
boolean flag;
System.out.print("Enter the size of the array: ");
n=sc.nextInt();
int arr[]=new int[n];
for(int i=0;i<n;i++)
{
	System.out.print("Enter number "+(i+1)+": ");
	arr[i]=sc.nextInt();
}
for(int i=0;i<n;i++)
{
	System.out.print(arr[i]+" ");
}
for(int i=0;i<n;i++)
{
flag=false;
if(arr[i]>arr[i+1])
{
temp=arr[i];
arr[i]=arr[i+1];
arr[i+1]=temp;
flag=true;
}

if(flag==false)
	break; 
}
for(int i=0;i<n;i++)
{
	System.out.println();
	System.out.print(arr[i]+" ");
}

}
}
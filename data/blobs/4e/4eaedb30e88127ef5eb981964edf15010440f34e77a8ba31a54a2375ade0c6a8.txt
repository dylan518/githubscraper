//Write a JAVA program to count number of digits in a number.  
import java.util.Scanner;
class CountDigits
  {
    public static void main(String[] args) 
    {

    int count = 0;
    Scanner sc=new Scanner(System.in);
    System.out.print("Enter number of digits: ");
    int n=sc.nextInt();
    while (n != 0) {
      n= n /10;
      count++;
    }

    System.out.println("Number of digits: " + count);
  }
}
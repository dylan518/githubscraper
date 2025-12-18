package Basics;

//Q4.Ask user for the year and display if it is leap year or non leap year
import java.util.Scanner;
public class Q4 {

public void  checkLeapYear() {
	Scanner sc = new Scanner(System.in);
     System.out.println("Enter a year:");
     int year =sc.nextInt();
     sc.close();

     if (year % 4 == 0 && year % 100 !=0 ||  year % 400 == 0) {

     		System.out.println(year + "is a Leap Year.");
     	
     }else{
     	System.out.println(year + "is not a Leap Year.");
     }
}

 public static void main(String[] args) {
        Q4 q4=new Q4();
        q4.checkLeapYear();
     
}
    
}

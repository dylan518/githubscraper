package aniket;

import java.util.Scanner;

public class ReverseNumber {
public static void main (String[] args) {
	Scanner sc = new Scanner(System.in);
	System.out.println("Enter a number");
	int n=sc.nextInt();
	while(n>0) {
		int d=n%10;
		System.out.print(d);
		n=n/10;
		
	}
}
}

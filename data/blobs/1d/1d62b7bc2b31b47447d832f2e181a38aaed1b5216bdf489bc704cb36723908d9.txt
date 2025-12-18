package com.important.program;

import java.util.Scanner;

public class PerfectNumberApp {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("enter a number");
		int n=scan.nextInt();
		int perfectNumber = PerfectNumber.perfectNumber(n);
		if(perfectNumber==n) {
			System.out.println("Entered number"+n+"is a perfect Number");
			
		}else {
			System.out.println("Entered number"+n+"is not a perfect Number");
		}
	
		
	}
	}
class PerfectNumber{
	static int perfectNumber(int n) {
		int sum=0;
		for(int i=1;i<n;i++) {
			if(n%i==0) {
			sum=sum+i;
			}
		}
	return sum;
	}
}


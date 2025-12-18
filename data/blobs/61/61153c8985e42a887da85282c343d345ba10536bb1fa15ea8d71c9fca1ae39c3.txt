package Numbers;

import java.util.Arrays;
import java.util.Scanner;

public class SumOfDigit {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("enter the number: ");
		long num = scanner.nextLong();
		
		long sum=0;
		while (num>0) {
			sum=sum+num%10;
			num=num/10;
		}
		System.out.println(sum);
	}
	

}

package application;

import java.util.Scanner;
import arraymath.Pairs;

public class Program {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("How many elements will the array have? ");
		int length = sc.nextInt();
		
		Pairs array = new Pairs(length);
		array.readValues(sc);
		
		array.averageCalc();
		array.print();
		
		sc.close();
	}

}

package patterns;

import java.util.Scanner;
//        1 
//      2 1 
//    3 2 1 
//  4 3 2 1 
//5 4 3 2 1 

public class Pattern19 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Value of n.");
		int n = sc.nextInt();
		for (int i = 1; i <= n; i++) {
			for (int sp = 1; sp <= n - i; sp++) {
				System.out.print("  ");
			}
			for (int j = i; j >= 1; j--) {
				System.out.print(j + " ");
			}
			System.out.println();
		}
	}

}

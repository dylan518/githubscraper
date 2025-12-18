package PATTERNPROGRAMS.Invertedtriangless;

import java.util.Scanner;

public class InvertedBinaryColumn {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("enter the number u want");
		int n;
		n = s.nextInt();
		int a = 0;
		for (int i = 1; i <= n; i++) {
			// Column loop
			for (int j = i; j <= n; j++) {
				System.out.print(((j + i) % 2) + " ");
			}
			System.out.println();
		}
	}

}

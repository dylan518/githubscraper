package uz.akbar;

import java.util.Arrays;
import java.util.Scanner;

public class App {
	public static void main(String[] args) {
		System.out.print("Massiv hajmini kiriting: ");
		Scanner sc = new Scanner(System.in);
		int length = sc.nextInt();
		int[] arr = new int[length];
		for (int i = 0; i < arr.length; i++) {
			System.out.print(i + 1 + "-elementni kiriting: ");
			int item = sc.nextInt();
			arr[i] = item;
		}
		System.out.println(Arrays.toString(arr));
		sc.close();
	}
}

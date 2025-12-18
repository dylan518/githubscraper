package Lab_01;

//Ho ten : Luong Hai Dang 
//Mssv: 20210151

import java.util.Scanner;

public class bai_6_3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap n:");
		int n = sc.nextInt();
		int stars = 1;
		int spaces = n-1;
		for(int s = 0;s<n;s++) {
		    for(int i = 0;i < spaces;i++) {
			System.out.print(" ");
			}
			for(int j = 1;j<=stars;j++) {
				System.out.print("*");
			}
			System.out.println();
			stars+=2;
			spaces--;
		}
	}
}

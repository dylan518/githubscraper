package Qize.Q596;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		int a = sc.nextInt();
		String[] str1 = str.split("");
		sc.close();

		if (str.length() < a) {
			for (int i = str.length() - 1; i >= 0; i--) {
				System.out.print(str1[i]);
			}
		} else {
			for (int i = str.length() - 1, c = 0; c < a; i--, c++) { // c는 뒤에서 부터 몇개를 출력할건지 나타내는 것
				System.out.print(str1[i]);							 // i는 str1 배열을 뒤에서부터 출력하려는 것
			}
		}
	}
}

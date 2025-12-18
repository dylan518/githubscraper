package com.kh.practice6.func;

import java.util.Scanner;

public class Practice5 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int x, y;
		while (true) {
			System.out.print("행 : ");
			x = sc.nextInt();
			sc.nextLine();
			if (x < 1 || x > 10) {
				System.out.println("1~10사이의 정수를 입력해주세요.");
			} else
				break;
		}

		System.out.println();

		while (true) {
			System.out.print("열 : ");
			y = sc.nextInt();
			if (y < 1 || y > 10) {
				System.out.println("1~10사이의 정수를 입력해주세요.");
			} else
				break;
		}
		sc.close();
		char[][] arr = new char[x][y];

		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				arr[i][j] = (char)(Math.random()*26 + 65); //65~90 나와야됑
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
	}
}

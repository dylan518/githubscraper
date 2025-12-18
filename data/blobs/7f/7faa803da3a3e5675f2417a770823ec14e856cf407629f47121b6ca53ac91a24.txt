package edu.kh.op.practice;

import java.util.Scanner;

public class OperatorPractice3 {

	public void practice1() {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("가격을 입력하세요 : ");
		int price = sc.nextInt();
		System.out.print("멤버십 있으세요? (있으면 true / 없으면 false 입력) : ");
		boolean member = sc.nextBoolean();
		double discount = (member == true)? price * 0.1 : price * 0.05;
		System.out.printf("할인을 포함한 최종금액 : %.1f\n", price - discount);
	}
	
	
	public void practice2() {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("출금할 금액 입력 : ");
		int amount = sc.nextInt();
		int count1 = amount / 50000; // 5만원권 갯수
		int count2 = (amount - (50000 * count1)) / 10000;
		int count3 = (amount - ((50000 * count1) + (10000 * count2))) / 5000;
		int count4 = (amount - ((50000 * count1) + (10000 * count2) + (5000 * count3))) / 1000;
		
		System.out.printf("50000원 : %d\n", count1);
		System.out.printf("10000원 : %d\n", count2);
		System.out.printf("5000원 : %d\n", count3);
		System.out.printf("1000원 : %d\n", count4);
	}
	
	
	public void practice3() {
		Scanner sc  = new Scanner(System.in);
		
		System.out.print("첫 번째 수 : ");
		int num1 = sc.nextInt();
		System.out.print("두 번째 수 : ");
		int num2 = sc.nextInt();
		
		String result = (num1 % num2 == 0) ? "배수입니다" : "배수가 아닙니다";
		System.out.println(result);
	}
}

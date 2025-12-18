package com.ajwalker.week03.diziler;
/*

Dizideki bir öğeyi arama
5 elemanlı elemanları kullanıcı tarafından girilen bir dizi oluşturun.
kullanıcının girdiği sayı dizide varsa BULUNDU, yoksa BULUNAMADI şeklinde mesaj versin
 */

import java.util.Scanner;

public class ArraySearch {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int nums[] = new int[5];
		int item = 0, userInput;
		
		do {
			System.out.print(item+ ". index degerini giriniz: ");
			nums[item] = sc.nextInt();
			item++;
		}while (item < nums.length);
		
		System.out.print("Dizi arama: ");
		userInput = sc.nextInt();
		
		//Flag mantığı
		boolean isFound = false;
		for (int value: nums){
			if (userInput == value){
				isFound = true;
				break;
			}
		}
		
		System.out.println(isFound? "BULUNDU":"BULUNAMADI");
	}
}
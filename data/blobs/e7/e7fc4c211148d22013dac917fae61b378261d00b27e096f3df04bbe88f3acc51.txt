package com.sp.javaprogram;

public class FindMinMaxArray {
	public static void main(String[] args) {

	
		int[] num = { 8, 5, 2, 1, 4, 7, 9, 6, 3 };

		int min = num[0];
		int max=num[0];

		for (int i = 1; i < num.length; i++) {
			if (num[i] < min) {
				min = num[i];
			}
			else if(num[i]>max) {
				max=num[i];
			}

		}
		
		System.out.println(min);
		System.out.println(max);
	}
}
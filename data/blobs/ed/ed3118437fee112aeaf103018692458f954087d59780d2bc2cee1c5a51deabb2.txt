package 일차원배열;

import java.util.Scanner;

public class 최댓값 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] arr = new int[9];
		
		for(int i = 0; i < 9; i++) {
			arr[i] = sc.nextInt();
		}
		
		int max = arr[0];
		int index = 1;
		
		for(int i = 0; i < 9; i++) {
			if(max < arr[i]) {
				max = arr[i];
				index = i+1;
			}
		}
		
		System.out.println(max);
		System.out.println(index);
	}
}

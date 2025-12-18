package silver.II;

import java.util.Scanner;

public class boj1699 {
	static int[] arr = new int[100001];
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int count = 0;

		/* Dynamic Programming - 중복되는 계산은 저장하기
		 1 : 1
		 2 : 2
		 3 : 3
		 4 : 1
		 5 : 2
		 6 : 3
		 7 : 4
		 8 : 2
		 9 : 1
		 10 : 2
		 11 : 3
		 */

		for (int i = 1; i <= N; i++) {
			arr[i] = i;
			for (int j = 1; j*j <= i; j++) {
				arr[i] = Math.min(arr[i], arr[i - j*j] + 1);
			}
		}
		System.out.println(arr[N]);
	}
}

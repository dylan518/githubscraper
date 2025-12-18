package CodeUp;

import java.util.Scanner;

public class 기초100제_1034 {

	public static void main(String[] args) {
		// [기초-출력변환] 8진 정수 1개 입력받아 10진수로 출력하기
		Scanner sc = new Scanner(System.in);
		String o = sc.nextLine();
		System.out.println(Integer.parseInt(o, 8));
	}
}

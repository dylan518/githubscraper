package javastudyS06;

import java.util.Scanner;

public class T0637 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the number : ");
		int number = input.nextInt();
		System.out.print("Enter the width : ");
		int width = input.nextInt();
		input.close();
		
		System.out.println(format(number, width));
	}

	public static String format(int number, int width) {
		
		String s = number + "";
		int length = s.length();
		
		if(s.length() < width) {
			for(int i = 1; i <= width - length; ++i) {
				s = "0" + s;
			}
		}
		
		return s;
	}
}

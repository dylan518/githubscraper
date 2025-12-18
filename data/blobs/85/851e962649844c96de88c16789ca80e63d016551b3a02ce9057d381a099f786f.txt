package com.Neotech.Review04;

public class MethodWithReturn {

	public static void main(String[] args) {

		String name = "Dardan";
		int numOfChars = name.length();

		System.out.println("The length of " + name + " is " + numOfChars);

		MethodWithReturn m = new MethodWithReturn();
		boolean res = m.isOdd(57);
		System.out.println("Is the number 57 odd? " + res);

		// printing in 1 step
		System.out.println("Is the number 90 odd? " + m.isOddEnhanced(90));

	} // outside of main method

	boolean isOdd(int num) {
		boolean result;
		if (num % 2 == 1) {
			result = true;
		} else {
			result = false;
		}
		return result;
	}

	// doing it in only 1 step
	boolean isOddEnhanced(int n) {
		return n % 2 == 1;
	}

}

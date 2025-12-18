package DigerKonular;

import java.util.Scanner;

public class PalindromicWords {

	public static void main(String[] args) {
		String word;
		
		Scanner scn = new Scanner(System.in);
		System.out.println("Please enter the word: ");
		word=scn.next();
		
		isPalindromicWord(word);
	}
	
	static void isPalindromicWord(String word) {
		String reverseWord = "";
		
		for(int i = word.length()-1; i>=0; i--) {
			reverseWord+=word.charAt(i);
		}
		
		if(word.equals(reverseWord))System.out.println("Palindromic word.");
		else System.out.println("Not a palindromic word.");
	}

}

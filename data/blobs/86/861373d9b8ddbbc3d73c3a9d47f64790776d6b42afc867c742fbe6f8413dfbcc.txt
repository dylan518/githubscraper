package com.vowelsandconsonants;

import java.util.HashSet;
import java.util.Iterator;

public class Alphabet {

	public static void main(String[] args) {

		String str = "Welcome";
		int vowelCount = uniqueVowel(uniqueCharacters(str));
		System.out.println("Vowel in the string are:" + vowelCount);

		int consonantCount = uniqueConsonant(uniqueCharacters(str));
		System.out.println("consonant in the string are:" + consonantCount);
	}

	public static int uniqueVowel(String str) {
		int count = 0;
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o'
					|| str.charAt(i) == 'u') {
				count++;
			}
		}
		return count;
	}

	public static int uniqueConsonant(String str) {
		int count = 0;
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) != 'a' && str.charAt(i) != 'e' && str.charAt(i) != 'i' && str.charAt(i) != 'o'
					&& str.charAt(i) != 'u') {
				count++;
			}
		}
		return count;
	}

	private static String uniqueCharacters(String str) {
		String uniqString = " ";
		HashSet<Character> set = new HashSet<>();
		for (int i = 0; i < str.length(); i++) {
			set.add(str.charAt(i));
		}
		Iterator<Character> itr = set.iterator();
		while (itr.hasNext()) {
			uniqString += itr.next();
		}
		return uniqString;
	}

}

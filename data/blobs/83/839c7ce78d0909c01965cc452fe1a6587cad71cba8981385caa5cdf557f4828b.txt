package com.toa;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class Program9 {

	public static void main(String[] args) {

			List<String> listofwords = Arrays.asList("lazy", "dog", "jumps", "over", "brown", "the", "fox");
			System.out.println(printlongestword(listofwords));
	}

		static boolean isBuildLongString(String s, boolean isorigword, HashMap<String, Boolean> mp) {
			
			if (mp.containsKey(s) && !mp.get(s))
				return false;

			if (mp.containsKey(s) && mp.get(s) && !isorigword) {
				return true;
			}
				for (int i = 1; i < s.length(); i++) {
					String left = s.substring(0, i);
					String right = s.substring(i);
						if (mp.containsKey(left) && mp.get(left) && isBuildLongString(right, false, mp)) {
							return true;
				}
			}
				mp.put(s, false);
				return false;
		}

		static String printlongestword(List<String> listofwords) {
			HashMap<String, Boolean> mp = new HashMap<>();
			for (String s : listofwords) {
				mp.put(s, true);
			}
				Collections.reverse(listofwords);
				for (String s : listofwords) {
					if (isBuildLongString(s, true, mp))
						return s;
				}
		return "No such string exists";
		}
}

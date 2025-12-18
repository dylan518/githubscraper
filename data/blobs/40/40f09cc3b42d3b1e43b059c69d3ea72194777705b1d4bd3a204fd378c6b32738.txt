package leetcode;

public class ConstructStringWithRepeatLimit {
	public static void main(String[] args) {
		System.out.println(repeatLimitedString("cczazcc", 3));
		System.out.println(repeatLimitedString("aababab", 2));
	}

	public static String repeatLimitedString(String s, int repeatLimit) {
		int[] freq = new int[26];
		
		for (char c : s.toCharArray()) {
			freq[c - 'a']++;
		}
		
		StringBuilder res = new StringBuilder();
		
//		repeatLimit -> 2
//		a -> 4
//		b -> 3
		
		int currLimit = 0;
		
		for (int i = 25; i >= 0;) {
			
			if (currLimit == repeatLimit) {
				currLimit = 0;
				i--;
				continue;
			}
			
			while (freq[i] != 0 && currLimit < repeatLimit) {
				res.append((char) ('a' + i));
				freq[i]--;
				currLimit++;
			}
			
			if (currLimit == repeatLimit && freq[i] != 0) {
				for (int j = i - 1; j >= 0; j--) {
					if (freq[j] != 0) {
						res.append((char) ('a' + j));
						freq[j]--;
						currLimit = 0;
						break;
					}
				}
			}
			
			if (freq[i] == 0) {
				currLimit = 0;
				i--;
			}
		}
		
		return res.toString();
	}
}

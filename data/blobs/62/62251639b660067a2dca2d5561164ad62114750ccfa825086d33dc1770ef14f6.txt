package cracking_the_coding_interview.array_and_strings;

import java.util.HashMap;

public class PalindromePermutation {

    public static void main(String[] args) {

        System.out.println( canPermutePalindrome("tactcoa"));
    }

   static public boolean canPermutePalindrome(String s) {
        HashMap<Character, Integer> map = new HashMap<> ();
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
            System.out.println(map.getOrDefault(s.charAt(i),0));
        }
        int count = 0;
        for (char key: map.keySet()) {
            count += map.get(key) % 2;
        }

        return count <= 1;
    }
}

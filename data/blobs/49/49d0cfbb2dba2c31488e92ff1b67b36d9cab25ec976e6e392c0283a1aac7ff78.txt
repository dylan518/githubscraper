package alogorithm_part2.sort;

import java.util.Arrays;

public class ValidAnagram {
    public static void main(String[] args) {
        String s = "anagram", t= "nagarma";
        boolean equals = sort(s).equals(sort(t));
        System.out.println("equals = " + equals);
    }

    public static String sort(String s) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }
}

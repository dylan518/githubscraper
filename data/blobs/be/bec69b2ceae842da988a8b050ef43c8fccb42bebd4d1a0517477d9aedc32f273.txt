package com.algorithm.leetcode.algorithm;

import java.util.Arrays;

public class ReverseString {

    public static void main(String[] args) {
        char[] s = {'h', 'e', 'l', 'l', 'o'};
//        char[] s = {'H', 'a', 'n', 'n', 'a', 'h'};
        reverseString(s);
    }

    public static void reverseString(char[] s) {
        for (int i = 0, j = s.length - 1; i < j; i++, j--) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }
        System.out.println(Arrays.toString(s));
    }
}
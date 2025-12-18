package com.dsa.string;

public class Palindrome {
    public static boolean isPalindrome(String str) {
        int start = 0, end = str.length()-1;
        str = str.toLowerCase();
        while(start <= end) {
            if(str.charAt(start) != str.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }
    public static void main(String[] args) {
        String str = "Saptarshi";
        System.out.println(isPalindrome(str));
    }
}

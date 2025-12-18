package com.strings;

public class ReverseString {
    public static void main(String[] args) {
        // 4 ways to reverse a string
        String s = "12345";
        // way1 - using toCharArray() method of string class
        char[] charArray = s.toCharArray();
        int start = 0, end = charArray.length - 1;
        while (start < end) {
            char temp = charArray[start];
            charArray[start] = charArray[end];
            charArray[end] = temp;
            start++;
            end--;
        }
        System.out.println(new String(charArray));

        // way2 - using charAt() method of string class
        StringBuilder rev = new StringBuilder();
        for(int i=s.length()-1 ; i>=0 ; i--){
            rev.append(s.charAt(i));
        }
        System.out.println(rev);

        // way3 - using StringBuffer
        System.out.println(new StringBuffer(s).reverse());

        // way4 - using StringBuilder
        System.out.println(new StringBuilder(s).reverse());
    }
}

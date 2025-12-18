package com.code;

public class Alphabet {

    public static String removeDuplicateChars(String input) {
        StringBuilder result = new StringBuilder();
        int length = input.length();
        for (int i = 0; i < length; i++) {
            char currentChar = input.charAt(i);
            if (i + 2 < length && currentChar == input.charAt(i + 1) && currentChar == input.charAt(i + 2)) {
                i=i+2;
                continue;
            }
            result.append(currentChar);
        }
        return result.toString();
    }

    public static void main(String[] args) {
        String input = "aabcccbbad";
        while (true){
            String tmp=input;
            input = removeDuplicateChars(input);
            if (tmp.equals(input)) {
                return;
            }
            System.out.println(input);
        }


    }
}

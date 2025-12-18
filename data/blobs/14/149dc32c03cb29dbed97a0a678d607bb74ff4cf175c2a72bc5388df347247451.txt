package org.training.stringPrograms;

public class ReverseAString {
    public static void main(String[] args) {
        String str = "I am a automation tester";
        char c = 'i';
        //retset a ma I
        char[] carr = str.toCharArray();
        String reverseStr = "";
        for (int i = carr.length - 1; i >= 0; i--) {
            reverseStr = reverseStr + carr[i];
        }
        System.out.println(reverseStr);
    }
}

package src.codes.recursion.rec_7_questions;

import java.util.ArrayList;
import java.util.List;

public class PhoneNo {
    public static void main(String[] args) {
//        char a = 'a' + 1; // b
//        int b = 'a' + 1;  // 98

        numpad("", "12");
        System.out.println();
        System.out.println(pad("", "12"));
        System.out.println(padCount("", "12"));
    }

    static void numpad(String p, String up) {
        if (up.isEmpty()) {
            System.out.print(p + " ");
            return;
        }

        int digit = Integer.parseInt(String.valueOf(up.charAt(0)));
        for (int i = (digit - 1) * 3; i < digit * 3; i++) {
            char ch = (char) ('a' + i);
            numpad(p + ch, up.substring(1));
        }
    }

    static List<String> pad(String p, String up) {
        if (up.isEmpty()) {
            List<String> list = new ArrayList<>();
            list.add(p);
            return list;
        }
        List<String> list = new ArrayList<>();
        int digit = Integer.parseInt(String.valueOf(up.charAt(0)));
        for (int i = (digit - 1) * 3; i < digit * 3; i++) {
            char ch = (char) ('a' + i);
            List<String> ans = pad(p + ch, up.substring(1));
            list.addAll(ans);
        }
        return list;
    }

    static int padCount(String p, String up) {
        if (up.isEmpty()) {
            return 1;
        }
        int count = 0;
        int digit = Integer.parseInt(String.valueOf(up.charAt(0)));
        for (int i = (digit - 1) * 3; i < digit * 3; i++) {
            char ch = (char) ('a' + i);
            int ans = padCount(p + ch, up.substring(1));
            count += ans;
        }
        return count;
    }

}

package pepcoding.backtracking.practice;

import java.util.HashSet;
import java.util.Set;

public class WordBreak {
    public static void main(String[] args) {
        HashSet<String> dict =new HashSet<>();
        dict.add("micro");
        dict.add("soft");
        dict.add("microsoft");
        dict.add("hi");
        dict.add("ring");
        dict.add("hiring");
        solution("microsofthiring", "",dict);

    }

    static void solution(String str, String ans, Set<String> dict) {
        if (str.isEmpty()) {
            System.out.println(ans);
            return;
        }
        for (int i = 0; i < str.length(); i++) {
            String left = str.substring(0, i + 1);
            if (dict.contains(left)) {
                String right = str.substring(i + 1);
                solution(right, ans + left + " ", dict);
            }
        }
    }
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class WordBreak {
    static int solve(String a, ArrayList<String> b, HashMap<String, Integer> dp) {
        if (b.contains(a))
            return 1;
        if (dp.containsKey(a))
            return dp.get(a);

        for (int k = 1; k < a.length(); k++) {
            String s1 = a.substring(0, k);
            String s2 = a.substring(k);
            if (b.contains(s1) && (b.contains(s2) || solve(s2, b, dp) == 1)) {
                dp.put(a, 1);
                return 1;
            }
        }
        dp.put(a, 0);
        return 0;
    }

    public static int wordBreak(String A, ArrayList<String> B) {
        HashMap<String, Integer> dp = new HashMap<>();
        return solve(A, B, dp);
    }

    public static void main(String[] args) {
        ArrayList<String> b = new ArrayList<>(Arrays.asList("i", "like", "sam",
                "sung", "samsung", "mobile",
                "ice", "cream", "icecream",
                "man", "go", "mango"));
        String a = "ilikesamsung";
        System.out.println(wordBreak(a, b));
    }
}

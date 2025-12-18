//{ Driver Code Starts
//Initial Template for Java

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n;
            n = sc.nextInt();
            ArrayList<String> arr = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                String p = sc.next();
                arr.add(p);
            }
            String line = sc.next();
            Sol obj = new Sol();
            System.out.println(obj.wordBreak(line, arr));

        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Sol {
    public int wordBreak(String s, ArrayList<String> B) {
        //code here
        HashSet<String> dictionary = new HashSet<>(B);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];

        for (int i = 0; i <= n; ++i) {
            if (dictionary.contains(s.substring(0, i))) {
                dp[i] = true;
                continue;
            }
            for (int j = 0; j < i; ++j) {
                if (dp[j] && dictionary.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n] ? 1 : 0;
    }
}
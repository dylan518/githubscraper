import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class BruteForce {
    public int lengthOfLongestSubstring(String s) {
      
        Set<Character> hs = new HashSet<>();
        int i = 0;
        int j = 0;
        int ans = 0; 

        while(j<s.length()) {
            if(!hs.contains(s.charAt(j))) {
                hs.add(s.charAt(j));
                j++;
                ans = Math.max(hs.size(), ans);
            }
            else {
                hs.remove(s.charAt(i));
                i++;
            }
        }

        return ans;
    }
    public static void main(String[] args) {
        Scanner ss = new Scanner(System.in);

        String str1 = ss.nextLine();

        BruteForce obj1 = new BruteForce();

        System.out.println(obj1.lengthOfLongestSubstring(str1));

    }
}

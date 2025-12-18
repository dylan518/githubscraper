package easy.twoPointers.Q0125ValidPalindrome;

/*

https://leetcode.com/problems/valid-palindrome/description/

Topics: Two Pointers, String

Time: O(n)
Space: O(1)

 */

public class Solution {
    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;

        while (l < r) {
            //Skip non-alphanumerics
            while (l < r && !Character.isAlphabetic(s.charAt(l)) && !Character.isDigit(s.charAt(l))) {
                l++;
            }
            while (l < r && !Character.isAlphabetic(s.charAt(r)) && !Character.isDigit(s.charAt(r))) {
                r--;
            }

            //Compare characters ignoring case
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }

            //Advance pointers
            l = l + 1;
            r = r - 1;
        }

        return true;
    }
}

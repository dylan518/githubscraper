class Solution {
    public int countSubstrings(String s) {
        var chars = s.toCharArray();
        var len = chars.length;
        var r = 0;

        // start will be our starting poin - the middle of palindromic substring
        for (int start = 0; start < len; start++) {
            int left;
            int right;

            // consider substrings with odd lenghts and
            // expand outwards from the same point
            left = start;
            right = start;
            while (left >= 0 && right < len && chars[left] == chars[right]) {
                r++;
                left--;
                right++;
            }

            // consider substrings with even lenghts and
            // expand outwards from adjacent points
            left = start;
            right = start + 1;
            while (left >= 0 && right < len && chars[left] == chars[right]) {
                r++;
                left--;
                right++;
            }
        }

        return r;
    }
}
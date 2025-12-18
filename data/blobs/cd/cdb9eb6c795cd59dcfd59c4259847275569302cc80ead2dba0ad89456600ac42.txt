public class KMPAlgo {

    // Function to search for a pattern in the text using the KMP algorithm its like
    // 2 pointer approach
    public static int KMPSearch(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();

        // Compute the longest prefix suffix array (LPS array)
        int[] lps = computeLPSArray(pattern);

        int i = 0; // index for text
        int j = 0; // index for pattern
        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }

            if (j == m) {
                System.out.println("Pattern found at index " + (i - j));
                j = lps[j - 1];
                return (i - j); // Return the first match position
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return -1; // Pattern not found
    }

    // Function to compute the LPS array
    public static int[] computeLPSArray(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int length = 0; // length of the previous longest prefix suffix
        int i = 1;

        lps[0] = 0; // LPS for the first character is always 0

        // Build the LPS array
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(length)) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    // Main function to test the KMP algorithm
    public static void main(String[] args) {
        String text = "abxabcabcaby";
        String pattern = "abcaby";
        int index = KMPSearch(text, pattern);

        if (index != -1) {
            System.out.println("Pattern found at index: " + index);
        } else {
            System.out.println("Pattern not found");
        }
    }
}

package Arrays;

public class stringcompression {

    public static String compressedString(String word) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        int n = word.length();

        while (i < n) {
            char currentChar = word.charAt(i);
            int count = 0;

            // Count the occurrences of the current character
            while (i < n && word.charAt(i) == currentChar) {
                count++;
                i++;
            }

            // Append the counts to the string builder
            while (count > 9) {
                sb.append(9).append(currentChar);
                count -= 9;
            }

            if (count > 0) {
                sb.append(count).append(currentChar);
            }
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(compressedString("abcde")); // Output should be 9a5a2b
    }
}

import java.util.ArrayList;

public class NumbersInString {

    private static final String IGNORE_CHARS = ".,$%+-?/";


    public static ArrayList<String> getNumbersInString(String line, boolean ignoreSpecialChars) {
        ArrayList<String> numList = new ArrayList<>();
        boolean inDigit = false;
        int startIndex = 0;
        char ch = ' ';
        for (int i = 0; i < line.length(); i++) {
            ch = line.charAt(i);

            if (IGNORE_CHARS.contains(ch + "") && ignoreSpecialChars)
                continue;

            if (Character.isDigit(ch)) {
                if (!inDigit) {
                    startIndex = i;
                }
                inDigit = true;

            } else {
                if (inDigit) {
                    numList.add(line.substring(startIndex, i));
                }
                inDigit = false;
            }
        }

        if (inDigit) {
            numList.add(line.substring(startIndex));
        }

        return numList;
    }

}

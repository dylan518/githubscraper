public class  ValidParenthesis {
    public static boolean isString(String s) {
        int lengthOfString = s.length();
        for (int j = 0; j < lengthOfString / 2; j++) {
            if (s.length() == 0) {
                return true;
            } else {
                if (s.contains("()")) {
                    s = s.replace("()", "");
                }
                if (s.contains("[]")) {
                    s = s.replace("[]", "");
                }
                if (s.contains("{}")) {
                    s = s.replace("{}", "");
                }
            }
        }

        System.out.println(s.length());
        if (s.length() == 0) {
            return true;
        } else {
            return false;
        }
    }
}

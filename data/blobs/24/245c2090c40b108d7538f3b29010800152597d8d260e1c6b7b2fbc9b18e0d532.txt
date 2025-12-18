/*
1) Simply removing all the leading whitespaces, and if index becomes greater than length it 
means string has only whitespaces
2) Checking the sign, if present
3) Now loop until the end of string and if any charcter except digit comes break the loop
4) Make the number, but also check if reaches beyond Integer limits [-2^31, 2^31-1].
5) If yes, then returns from there only, no need to iterate futher.
6) In the end return no. with the sign
*/
class Solution {

    public int myAtoi(String s) {
        s = s.trim();
        boolean negative = false;
        long num = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (i == 0 && c == '-') {
                negative = true;
            } else if (i == 0 && c == '+') {
                negative = false;
            } else {
                if (Character.isDigit(c)) {
                    num = num * 10 + Character.getNumericValue(c);
                    if (num > Integer.MAX_VALUE && negative) {
                        return Integer.MIN_VALUE;
                    }
                    else if (num > Integer.MAX_VALUE) {
                        return Integer.MAX_VALUE;
                    }
                } else {
                    break;
                }
            }
        }
        if (num == 0) {
            return 0;
        }
        System.out.println("num = " + num);
        if (negative == true) {
            num = 0 - num;
        }
        
        return (int) num;
    }
}

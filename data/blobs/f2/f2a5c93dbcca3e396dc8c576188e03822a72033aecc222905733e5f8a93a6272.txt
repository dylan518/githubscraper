public class Solution {
    public String solution(String myString, String pat) {
        int lastIndex = myString.lastIndexOf(pat) + pat.length();
        String answer = myString.substring(0, lastIndex);
        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String myString = "AbCdEFGdE";
        String pat = "dE";
        String answer = sol.solution(myString, pat);
        System.out.println("answer = " + answer);
    }
}

package org.rosemwal.dsa.string;

public class StringRotation55 {

    public static void main(String[] args)  {

        String s = "abcde";
        String goal = "cdeab";

        System.out.println(isRotationUsingSubstring(s,goal)); // O(n*n)
        System.out.println(isRotationUsingConcat(s, goal)); // O(n)

    }

    private static boolean isRotationUsingConcat(String s, String goal) {

        String concatString = s+s;
        if (concatString.contains(goal)) {
            return true;
        }
        return false;
    }

    private static boolean isRotationUsingSubstring(String s, String goal) {

        int index = goal.indexOf(s.charAt(0));
        if (index == -1 || s.length() != goal.length())    {
            return false;
        }

        for(int i=0; i<s.length(); i++) {

            if (goal.charAt(i) != s.charAt(0))  {
                continue;
            }

            String goalFirstHalf = goal.substring(0, i);
            String goalSecondHalf = goal.substring(i);

            if (goalFirstHalf.equals(s.substring(goal.length() - i))
                    && goalSecondHalf.equals(s.substring(0, goal.length() - i)))  {
                return true;
            }
        }
        return false;
    }
}

package com.company.lv0.day_240301;

// https://school.programmers.co.kr/learn/courses/30/lessons/181934
public class Q3_조건문자열 {

    private static String ineq = "<";
    private static String eq = "=";
    private static int n = 20;
    private static int m = 50;

    public static void main(String[] args) {
        int answer = 0;

        if (ineq.equals("<")) {
            if (eq.equals("=")) answer = n <= m ? 1 : 0;
            else answer = n < m ? 1 : 0;
        } else {
            if (eq.equals("=")) answer = n >= m ? 1 : 0;
            else answer = n > m ? 1 : 0;
        }

        System.out.println("answer = " + answer);
    }
}

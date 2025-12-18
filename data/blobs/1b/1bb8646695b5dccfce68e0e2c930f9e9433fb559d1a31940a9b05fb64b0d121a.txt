package com.faang.me.apnacollege.arrays2D;

/**
 *
 * Created by Mohammad Shakir - 11/04/2023
 */
public class $02_DiagonalSum {

    /**
     * Time Complexity - O(n^2) Space Complexity - O(n)
     *
     * @param a
     * @return
     */
    public static int diagonalSum(int[][] a) {
        int sum = 0;
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[0].length - 1; j++) {
                if (i == j) {
                    // primary diagonal
                    sum += a[i][j];
                } else if (i + j == a.length - 1) {
                    // Secondary Diagonal
                    sum += a[i][j];
                }
            }
        }
        return sum;
    }

    public static int diagonalSumBetter(int[][] a) {

        int sum = 0;
        for (int i = 0; i < a.length - 1; i++) {
            // Primary diagonal
            sum += a[i][i];

            // secondary diagonal
            // i + j = n - 1 => i = n - 1 - j
            if (i != a.length - i - 1) {
                sum += a[i][a.length - i - 1];
            }
        }
        return sum;
    }

    public static void main(String[] args) {

    }
}

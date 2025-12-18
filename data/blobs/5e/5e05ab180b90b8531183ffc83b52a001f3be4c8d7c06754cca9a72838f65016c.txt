package com.dynamicprogamming;

import java.util.HashMap;
import java.util.List;

public class CountPaths {
    public static void main(String[] args) {
        int[][] arr = {{1, 2, 3},
                       {4, 5, 6},
                       {7, 8, 9}};
        System.out.println(countPaths(arr, 0, 0, new HashMap<List<Integer>, Integer>()));

    }

    private static int countPaths(int[][] arr, int r, int c, HashMap<List<Integer>, Integer> memo) {

        if (r == arr.length - 1 && c == arr[r].length) {
            return 1;
        }
        if (r == arr.length || c == arr[r].length) {
            return 0;
        }

         if(arr[r][c] == 7) { // if there is a blocker
             return 0;
         }
        List<Integer> pos = List.of(r, c);
        if (memo.containsKey(pos)) {
            return memo.get(pos);
        }

        int result = countPaths(arr, r + 1, c, memo) + countPaths(arr, r, c + 1, memo);
        memo.put(pos, result);
        return result;


    }
}

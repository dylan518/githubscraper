package com.company;

import java.util.Scanner;

public class countSubsetSumWithGivenDiffDP21 {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = scn.nextInt();
        }
        int diff = scn.nextInt();
        int count = countSubsetSumWithGivenDiff(arr, diff);
        System.out.println(count);
    }
    public static int countSubsetSumWithGivenDiff(int[] arr, int diff){
        if(arr.length == 0){
            return 0;
        }
        int sum = 0;
        for(int i : arr){
            sum += i;
        }
        int s1 = (diff + sum)/2;
        return countSubsetSum21(arr, s1);
    }
    public static int countSubsetSum21(int[] arr, int s1){
        if(s1 == 0){
            return 1;
        }else if(arr.length == 0){
            return 0;
        }
        int[][] dp = new int[arr.length+1][s1+1];
        for(int i = 0; i < arr.length+1; i++){
            dp[i][0] = 1;
        }
        for(int i = 1; i < s1+1; i++){
            dp[0][i] = 0;
        }
        for(int i = 1; i < arr.length+1; i++){
            for(int j = 1; j < s1+1; j++){
                if(arr[i-1] <= j){
                    dp[i][j] = dp[i-1][j - arr[i-1]] + dp[i-1][j];
                } else{
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[arr.length][s1];
    }
}

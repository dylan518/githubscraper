package com.practice.java.Arrays;

public class MissingElement {
    public static void main(String[] args) {
        int[] arr = new int[]{1,2,3,5};
        System.out.println(missingNumber(5,arr));
    }

    static int missingNumber(int n, int arr[]) {
        int expSum = n*(n+1)/2;
        // Your Code Here
        int actualSum = 0;
        for(int i:arr){
            actualSum+=i;
        }
        return expSum - actualSum;
    }
}

package com.arrays;

import java.util.Arrays;

public class MergeSortedSubarrays {
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9, 11, 0, 4, 6, 8};

        int endIndex = 5;
        merge(arr, endIndex);
    }

    static void merge(int[] arr, int endIndex) {

        int[] B = Arrays.copyOfRange(arr, endIndex + 1, arr.length);
        System.out.println(Arrays.toString(B));

        System.out.print(Arrays.toString(arr));


        int len = endIndex + 1 + B.length;
        System.out.println("len" + len);
        int[] C = new int[len];
        int i = endIndex;

        int j = B.length - 1;
        int k = len - 1;
        System.out.println("i" + i + "j" + j + "k" + k);

        while (i >= 0 && j >= 0) {
            if (arr[i] > B[j]) C[k--] = arr[i--];
            else C[k--] = B[j--];
        }
        while (i >= 0) {
            C[k--] = arr[i--];
        }
        while (j >= 0) {
            C[k--] = B[j--];
        }

        System.arraycopy(C, 0, arr, 0, arr.length);


        System.out.print(Arrays.toString(arr));

    }

}





//class Solution {
//    void merge (int[] arr, int endIndex) {
//        int subarr1Current = 0, subarr2Current = endIndex + 1;
//        int[] ans = new int[arr.length];
//        int ansIndx = 0;
//        while (subarr1Current <= endIndex && subarr2Current < arr.length) {
//            if(arr[subarr1Current] < arr[subarr2Current]) {
//                ans[ansIndx++] = arr[subarr1Current++];
//            } else {
//                ans[ansIndx++] = arr[subarr2Current++];
//            }
//        }
//        while (subarr1Current <= endIndex) {
//            ans[ansIndx++] = arr[subarr1Current++];
//        }
//        while (subarr2Current < arr.length) {
//            ans[ansIndx++] = arr[subarr2Current++];
//        }
//        for (int i = 0; i < arr.length; i++) {
//            arr[i] = ans[i];
//        }
//    }
//}

package com.pro.array;
/*
Program to cyclically rotate an array by one
Given an array, cyclically rotate the array clockwise by one.

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}
 */

import com.pro.util.ArrayUtil;

public class CyclicallyRotate {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        clockWiseRotation(arr);
        ArrayUtil.displayArray(arr);

        antiClockWiseRotation(arr);
        ArrayUtil.displayArray(arr);
    }

    private static void antiClockWiseRotation(int[] arr) {
        int n= arr.length;
        int temp=arr[0];
        for(int i=0;i<n-1;i++){
            arr[i]=arr[i+1];
        }
        // place the first element of the array at the end index.
        arr[n-1]=temp;
    }

    private static void clockWiseRotation(int[] arr) {
        int n = arr.length;
        int temp = arr[n-1];
        for(int i=n-1;i>0;i--){
            arr[i]=arr[i-1];
        }
        // place the last element in Oth index.
        arr[0] = temp;
    }
}

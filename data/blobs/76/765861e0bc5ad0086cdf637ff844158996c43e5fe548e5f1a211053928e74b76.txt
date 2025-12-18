package com.geeksforgeeks.mytest.binarysearch;

import android.util.Log;

public class SortArray {

    public int[] sort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                int temp = 0;
                if(arr[i] > arr[j]){
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        return arr;
    }

    public void main() {
        int[] arr = {7, 2, 4, 1, 19, 15, 24, 12};
        int[] a = sort(arr);
        Log.e("mytestt", "binary asc " + a);
    }


}

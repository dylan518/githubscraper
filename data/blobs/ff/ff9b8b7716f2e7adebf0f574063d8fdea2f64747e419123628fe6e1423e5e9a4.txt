package com.dsalgo.arrays.threewaypartition;

/**
 * Problem Link: https://leetcode.com/problems/sort-colors/submissions/
 * Solved using 3 pointers for each letter
 * Time: O(N)
 */
class Sort012 {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length-1;
        //move mid-pointer till high
        while(mid <= high){
            switch(nums[mid]){
                case 0:
                    swap(nums, low, mid); // if mid points to 0 then swap it with element at low
                    low++;      // increment low to point next element as current element at low is sorted
                    mid++;      // increment mid to process next element
                    break;
                case 1:         // if mid point's to 1 means 1 is at right position
                    mid++;      // increment mid
                    break;
                case 2:         // if mid points to 2 means it's not at right position so replace with position of high
                    swap(nums, mid, high);
                    high--;
                    break;
            }
        }
    }

    void swap(int[] nums, int i, int j){
        int temp =  nums[i];
        nums[i] = nums[j];
        nums[j] =  temp;
    }
}
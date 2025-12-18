package com.problemsolving.leetcode.easy;

/**
 * 26. Remove Duplicates from Sorted Array
 * Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
 *
 * @author Mohammed Abdelkawy
 * @version 1.0.0
 * @since 23.08.2022
 */
public class RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        int insertedIndex = 1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[i - 1]){
                nums[insertedIndex] = nums[i];
                insertedIndex++;
            }
        }
        return insertedIndex;
    }
}

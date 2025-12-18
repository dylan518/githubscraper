package com.lbnbhl.leetcode.offer2;

/**
 * @autor wwl
 * @date 2023/1/22-20:22
 */
public class Offer12 {
    public int pivotIndex1(int[] nums) {
        int sum=0,left=0;
        for (int num : nums) {
            sum += num;
        }

        if (sum-nums[0]==0) return 0;

        for (int i = 1; i < nums.length; i++) {
            left+=nums[i-1];
            int right=sum-nums[i]-left;
            if (right == left)
                return i;
        }
        return -1;
    }

    public int pivotIndex2(int[] nums) {
        int sum=0,left=0;
        for (int i = nums.length-1; i >=0; i--) {
            sum+=nums[i];
        }

        if (sum-nums[0]==0) return 0;

        for (int i = 1; i < nums.length; i++) {
            left+=nums[i-1];
            int right=sum-nums[i]-left;
            if (right == left)
                return i;
        }
        return -1;
    }
}

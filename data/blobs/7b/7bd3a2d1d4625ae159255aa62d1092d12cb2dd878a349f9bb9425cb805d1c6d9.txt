package com.ln.code.array;

/**
 * 209.长度最小的子数组
 * 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
 */
public class num209长度最小的子数组 {
    public static int minSubArrayLen1(int s, int[] nums) {
        int left = 0;
        int sum = 0;
        int result = Integer.MAX_VALUE;
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];
            while (sum >= s) {
                result = Math.min(result, right - left + 1);
                sum -= nums[left++];
            }
        }
        return result == Integer.MAX_VALUE ? 0 : result;
    }

    public static int minSubArrayLen(int s,int[] arr){
        int right;
        int left = 0;
        int sum = 0;
        int len = arr.length;
        int result = Integer.MAX_VALUE;
        for (right = 0; right < len; right++) {
            sum += arr[right];
            while(sum >= s){
                result = Math.min(result, right - left + 1);
                sum -= arr[left++];
            }
        }
        return result == Integer.MAX_VALUE ? 0 : result;
    }

    public static void main(String[] args) {
        int[] arr = {1,4,2,7,8,3,2};
        System.out.println(minSubArrayLen(14,arr));
    }
}
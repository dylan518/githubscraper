package com.BinarySearch;
// first and last element in sorted array
import java.util.Arrays;
import java.util.Scanner;

public class FALEISA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = {1,2,3,4,5,3,1};
        int target = 3;
        int[] ans = {-1, -1};

        int start = search(nums,target,true);
        int end = search(nums,target,false);

        ans[0] = start;
        ans[1] = end;
        System.out.println(Arrays.toString(ans));
    }
//    static int[] searchRange(int[] nums, int target) { Brute Force Method
//        for(int i=0; i<nums.length; i++){
//            for(int j=nums.length-1; j>=0; j--){
//                if(nums[i] == target && nums[j] == target){
//                    return new int[] {i, j};
//                }
//            }
//        }
//        return new int [] {-1,-1};
//    }



    static int search(int[] nums, int target, boolean findStartSymbol){
        int ans = -1;
        int start = 0;
        int end = nums.length-1;

        while(start <= end){
            int mid = start + (end-start)/2;
            if(target < nums[mid]){
                end = mid - 1;
            } else if (target > nums[mid]){
                start = mid + 1;
            } else {
                ans = mid;
                if(findStartSymbol){
                    end = mid -1;
                } else {
                    start = mid + 1;
                }
            }

        }
        return ans;
    }
}

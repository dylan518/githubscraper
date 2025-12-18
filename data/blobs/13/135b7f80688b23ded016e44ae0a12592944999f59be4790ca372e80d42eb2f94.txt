package Target100In30DaysEnd16JanLeetCode.prefixSum.easy;
/**
 * Question 303
 *Given an integer array nums, handle multiple queries of the following type:
 *
 * Calculate the sum of the elements of nums between indices left and right inclusive where left
 * <= right.
 * Implement the NumArray class:
 *
 * NumArray(int[] nums) Initializes the object with the integer array nums.
 * int sumRange(int left, int right) Returns the sum of the elements of nums between indices left
 * and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 * */
public class RangeSumQuery_Immutable {
    int[] nums; // -2,-2,1,-4,-2,-3
    public RangeSumQuery_Immutable(int[] nums) { //-2, 0, 3, -5, 2, -1
        for (int i = 1; i < nums.length; i++) {
            nums[i] = nums[i-1]+nums[i];
        }
        this.nums = nums;
    }

    public int sumRange(int left, int right) {
        int val;
        if(left==0) return nums[right];
        else{
            val = nums[right]-nums[left-1];
        }
        return val;
    }
}

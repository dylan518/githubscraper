package Array.Easy;

import java.util.Arrays;

public class ArrayPartitionI {
    public static void main(String[] args) {
        ArrayPartitionI o = new ArrayPartitionI();

        System.out.println(
                Arrays.toString(
                        new int[]{
                                o.arrayPairSum(new int[]{1, 4, 3, 2}),
                                o.arrayPairSum(new int[]{6, 2, 6, 5, 1, 2})
                        }
                )
        );
        // [4, 9]
    }

    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int ans = 0;
        for (int i = 0; i < nums.length; i += 2)
            ans += nums[i];

        return ans;
    }
}

// https://leetcode.com/problems/array-partition-i/

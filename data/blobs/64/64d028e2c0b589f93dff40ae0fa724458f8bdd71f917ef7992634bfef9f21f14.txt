package arrayCodes;

import java.util.Arrays;

public class MissingInRange {
    public static int findMissing(int[] nums) {
        int n = nums.length+1;
        int maxSum = n * (n + 1) / 2;
        int currSum = 0;

        for (int i = 0; i < nums.length; i++) {
            currSum += nums[i];
        }
        return maxSum - currSum;
    }
    public static void main(String[] args) {
        int[] nums={1,2,3,5,6};
        int result=findMissing(nums);
        System.out.println(result);
    }
}

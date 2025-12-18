class Solution {
    public static int[] productExceptSelf(int[] nums) {
        int[] out = new int[nums.length];
        int pfix = 1;

        for (int i = 0; i < nums.length; i++) {
            out[i] = pfix;
            pfix *= nums[i];
        }
        pfix = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            out[i] *= pfix;
            pfix *= nums[i];
        }

        return out;
    }
}
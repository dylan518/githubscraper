class Solution {

    public int[] productExceptSelf(int[] nums) {
        final int length = nums.length;
        final int[] ans = new int[length];

        int product = 1;
        for (int i = 0; i < length; i++) {
            ans[i] = product;
            product *= nums[i];
        }

        //System.out.println(Arrays.toString(ans));

        product = 1;
        for (int i = length - 1; i >= 0; i--) {
            ans[i] *= product;
            product *= nums[i];
        }

        return ans;
    }
}

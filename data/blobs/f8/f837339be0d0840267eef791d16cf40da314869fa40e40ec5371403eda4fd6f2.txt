class Solution {
    public long minimumReplacement(int[] nums) {
        long ans = 0;
        int n = nums.length, cur, nxt, count;

        for (int i = n - 2; i >= 0; i--) {
            cur = nums[i];
            nxt = nums[i+1];

            if (cur <= nxt) {
                continue;
            }

            count = (cur + nxt - 1) / nxt;
            ans += count - 1;
            nums[i] = cur / count;
        }

        return ans;
    }
}
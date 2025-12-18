/*
 * @lc app=leetcode.cn id=2091 lang=java
 *
 * [2091] 从数组中移除最大值和最小值
 * 
 * 61/61 cases passed (2 ms)
 * Your runtime beats 100 % of java submissions
 * Your memory usage beats 67.8 % of java submissions (48.8 MB)
 */

// @lc code=start
class Solution {
    public int minimumDeletions(int[] nums) {
        int min = 0;
        int max = 0;
        int n = nums.length;
        for(int i = 0; i < nums.length; i++) {
            if (nums[min] > nums[i]) min = i;
            if (nums[max] < nums[i]) max = i;
        }
        int left = Math.min(max, min);
        int right = Math.max(max, min);
        // 移除前n个       移除后n个       移除前n个&后n个 
        return Math.min(right + 1, Math.min(n - left, left + 1 + n - right));
    }
}
// @lc code=end


class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        
        int[] count = new int[1000001];
        int left = 0;
        int right = 0;
        long res = 0;
        while (right < nums.length) {
            count[nums[right]]++;
            while (count[nums[left]] > maxK) {
                count[nums[left]]--;
                left++;
            }
            int j = left;
            while (count[nums[j]] >= minK) {
                res += j - left + 1;
                j++;
            }
            right++;
        }
        return res;
    }
}
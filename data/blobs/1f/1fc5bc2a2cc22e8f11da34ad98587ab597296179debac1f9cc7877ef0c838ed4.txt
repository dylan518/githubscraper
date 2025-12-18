// https://leetcode.com/problems/binary-search/description/

class Solution {
    public int search(int[] nums, int target) {
        int l=0;
        int r = nums.length-1;
        while(r-l>1){
             int mid = (l+r)/2;
             if(nums[mid] < target)
                 l=mid+1;
             else 
                 r=mid;
        }
            if(nums[l]==target)
                return l;
            else if(nums[r]==target)
                return r;
            else 
                return -1;
    }
}
class Solution {
    public int maxAbsoluteSum(int[] nums) {
        
        int max=Math.abs(nums[0]);
        int prevMax=nums[0];
        int prevMin=nums[0];
        
        
        for(int i=1;i<nums.length;i++){
            prevMax=Math.max(nums[i],prevMax+nums[i]);
            prevMin=Math.min(nums[i],prevMin+nums[i]);
            max=Math.max(max,Math.max(Math.abs(prevMax),Math.abs(prevMin)));
            
        }
     return max;   
    }
}

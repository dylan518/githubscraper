class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        fun(0,nums,ans,ds,Integer.MIN_VALUE);
        return ans;
    }
    private void fun(int index,int[] nums,List<List<Integer>> ans,List<Integer>ds,int prev)
    {
        if(ds.size() > 1)
        {
                ans.add(new ArrayList<>(ds));
        }
        Set<Integer> seen = new HashSet<>();
            for(int i=index;i<nums.length;i++)
            {
                if(seen.contains(nums[i])) continue;
                if(nums[i] >= prev)
                {
                    seen.add(nums[i]);
                    ds.add(nums[i]);
                    fun(i+1,nums,ans,ds,nums[i]);
                    ds.remove(ds.size()-1);
                }
            }
    }
}
import java.util.Arrays;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hashNum = new HashMap<Integer,Integer>();
        //# of instructions = n
        for(int i=0 ;i<nums.length ;i++){
            hashNum.put(i,nums[i]);
        }
        int diff;
        for(int i=0 ;i<nums.length ;i++){
            diff = target - hashNum.get(i);
            if(hashNum.containsValue(diff)){
                for(int j=i+1;j<nums.length;j++){
                    if(hashNum.get(j) == diff) return new int[] {i,j};
                }
            }
        }
        
        return null;
    }  
}

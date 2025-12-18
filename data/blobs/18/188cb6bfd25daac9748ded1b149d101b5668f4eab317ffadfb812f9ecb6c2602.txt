class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
           List<Integer> missingNumbers = new ArrayList<>();
        
        // Step 1: Mark present numbers
        for (int i = 0; i < nums.length; i++) {
            int num = Math.abs(nums[i]);
            if (nums[num - 1] > 0) {
                nums[num - 1] = -nums[num - 1];
            }
        }
        
        // Step 2: Find all numbers which are not marked
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missingNumbers.add(i + 1);
            }
        }
        
        return missingNumbers;
    }
}
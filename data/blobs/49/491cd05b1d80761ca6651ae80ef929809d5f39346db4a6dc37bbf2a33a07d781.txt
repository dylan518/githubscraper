import java.util.Scanner;

class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int left = 0;
        int right = nums.length-1;

        while(left <= right){
            int mid = left + (right  - left) / 2;
            if(nums[mid] == target){
                return mid;
            }else if (nums[mid] < target){
                left = mid + 1;
            }else {
                right = mid - 1;
            }
        }
        return left;
        
    }

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        int x = scan.nextInt();
        int[] num = new int[x];

        for(int i = 0; i < x; i++){
            num[i] = scan.nextInt();
        } 

        int targets = scan.nextInt();

        Solution sol = new Solution();
        int result = sol.searchInsert(num, targets);

        System.out.println(result);
    }
}
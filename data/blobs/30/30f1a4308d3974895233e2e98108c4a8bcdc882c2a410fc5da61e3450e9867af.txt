package solutions.newTest;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {-4,-1,0,3,10};

        System.out.println(Arrays.toString(Solution.sortedSquares(arr)));
    }
}

class Solution {
    public static int[] sortedSquares(int[] nums) {
        int head = 0;
        int tail = nums.length-1;
        int[] arr = new int[nums.length];

        for(int i = 0; i < nums.length; i++){
            nums[i] = nums[i] * nums[i];
        }

        int index  = nums.length - 1;
        while(true){
            if(head == tail){
                arr[index] = nums[head];
                break;
            }

            if(nums[head] >= nums[tail]){
                arr[index] = nums[head];
                head++;
                index--;

            }else {
                arr[index] = nums[tail];
                tail --;
                index--;
            }
        }

        return arr;
    }
}

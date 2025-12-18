import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
public class FirstAndLastPosition{
	
	//O(logn) = binary Search
	
	
	// solution 3
	public static int firstIndex(int[] nums, int target){
        int index = -1;
        int start = 0;
        int end = nums.length -1;
        
        while(start <= end){
            int mid = start + (end-start)/2;
            if(nums[mid] >= target){
                end = mid-1;
            }else{
                start = mid+1;
            }
            if(nums[mid] == target){
                index = mid;
            }
        }
        
        return index;
    }
    
    public static int secondIndex(int[] nums, int target){
        int index = -1;
        int start = 0;
        int end = nums.length-1;
        
        
        while(start <= end){
            int mid = start + (end-start)/2;
            if(nums[mid] <= target){
                start = mid+1;
            }else{
                end = mid-1;
            }
            if(nums[mid] == target){
                index = mid;
            }
        }
        
        return index;
    }
    
    
    public static int[] searchRange(int[] nums, int target) {
       int[] result = new int[2];
       result[0] = firstIndex(nums, target);
       result[1] = secondIndex(nums, target);
       return result;
        
    }
	
    public static void main(String[] args){
		
		int[] nums = {3,3,3};
		int target = 3;
		
		System.out.println(Arrays.toString(searchRange(nums,target)));

    }
}


/*//Solution 1
        int len = nums.length;
        int startingIndex = 0;
        int endingIndex = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < len; i++){
            int diff = target - nums[i];
            int indexValue = nums[i];
            if(len == 1 && diff == 0){
                return new int[] {0,0};
            }
            if(diff == 0){
                if(map.containsKey(indexValue)){
                    map.put(indexValue, map.get(indexValue) + 1);
                    endingIndex = i;
                }else{
                    map.put(nums[i], 1);
                    startingIndex = i;
                }
            }  
        }
        
        for(Map.Entry entry : map.entrySet())
            if((int)entry.getValue() == 1){
                return new int[] {startingIndex, startingIndex};
            }else if((int)entry.getValue() >= 2){
                return new int[] {startingIndex, endingIndex};
        }
        return new int[] {-1,-1};*/


/*
		//solution 2
		int len = nums.length;
        int startingIndex = 0, endingIndex = 0;
        for(int i = 0; i < len; i++){
            for(int j = len-1; j >= 0; j--){
                if(target - nums[i] == 0 && target - nums[j] == 0){
                    return new int[] {i,j};
                }
             }
         }

        return new int[] {-1,-1};*/
		
		
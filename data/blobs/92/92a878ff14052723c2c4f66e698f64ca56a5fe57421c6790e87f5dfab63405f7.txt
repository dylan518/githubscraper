import java.util.* ;
import java.io.*; 
public class Solution {	
	public static int minimumOperation(int[] arr, int n) {
		HashMap<Integer,Integer> map=new HashMap<>();
        for(int num:arr)
        {
            map.put(num,map.getOrDefault(num,0)+1);
        }
        int max=Collections.max(map.values());
        return n-max;
	}
}

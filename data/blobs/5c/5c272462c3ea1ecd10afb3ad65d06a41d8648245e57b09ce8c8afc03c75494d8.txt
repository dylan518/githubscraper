package basics.SlidingWindow;

import java.util.ArrayDeque;
import java.util.Deque;

public class FIrstNegative {
	
	public static void name(int [] arr, int k) {
		
		int i =0 ,j =0;
		Deque<Integer> dq = new ArrayDeque<Integer>();
		while(j<arr.length)
		{
			
			if(arr[j]<0)
			{
			
				dq.addLast(arr[j]);
			}
			
			
			if(j-i+1 <k)
			{
				j++;
			}else if(j-i+1==k)
			{
				if( dq.isEmpty() )
				{
					System.out.println(0);
					dq.addLast(0);
				}
				else
				{
					System.out.println(dq.peek());
					if(dq.peek() == arr[i] )
					{
						dq.pop();
						
					}
				}
				
				
				
				
				
				
				i++;
				j++;
				
			}
			
			//System.out.println(dq);
			
			
			
		}
		
		
	}
	
	
	
	public static void main(String[] args) {
		int[] arr = {12,-1,-7,8,-15,13,16,28};
		//-1, -1,-7, -15, -15, 0
		name(arr,3);
	}

}

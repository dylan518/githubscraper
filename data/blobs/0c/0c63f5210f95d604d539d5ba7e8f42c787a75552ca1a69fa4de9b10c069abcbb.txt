package Day1;

import java.util.ArrayList;

public class binaryTest {

	public static void main(String[] args) {
		//Solution.toSolve(1041);					//toSolve method is called from solution class.
		int count1= Solution.toSolve(1041);
		System.out.println("Max 0 count: "+count1);
		
		int count2= Solution.toSolve(88);
		System.out.println("Max 0 count: "+count2);

		int count3= Solution.toSolve(90);
		System.out.println("Max 0 count: "+count3);

	}
	
}
class Solution {
	public static int toSolve(int n) {
		String binaryForm= Integer.toBinaryString(n);		
		//converting decimal into binary form as binary is in string from we have to convert it to Integer.
		// toBinaryString will return String type but accepts int type arguments, hence we used Integer class.
	    
		System.out.println("Binary Representation of: "+n+" is "+binaryForm);	
		//printing conversion --> decimal to binary
		
		int longestGap=0;
		//Initialize with zero just to hold the data.
		
		ArrayList<Integer> onesList= new ArrayList<Integer>();
		//creating arrayList of type Integer class.
		
		for(int i=0;i<binaryForm.length();i++) {
			if (binaryForm.charAt(i)=='0') 
			//charAt --> for reading values; here in this if loop we read char as '0',when '1' comes loop breakes.
				continue;
			onesList.add(i);
			//when loop breaks '1' get added to onesList.
		}
		//0  1  2
		//0  6  10
		for(int i=0;i<onesList.size()-1;i++) {
			//size-1 bcozz there are two spaces if i=3(0 1 2);
			
			int indicesDifference= onesList.get(i+1)-onesList.get(i)-1;
			//here i=0,(0+6-0)-1= 5;  then i=1,(10-6-1)=3
			//          (data)  (spaces)	    (data)  (spaces)
			longestGap= Math.max(longestGap, indicesDifference);
			//max function from math class will return max value between two given parameters.
		}
		return longestGap;
	}
}
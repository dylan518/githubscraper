package Sy;

public class Sum_Array {

	public static void main(String[] args) {
		int [] arr={1,2,3,4,5,6,7};//sum=9 output pair found (2,7),(3,6),(4,5)
		int sum=0;
		for(int i=0; i<arr.length; i++) {
			for(int j=i+1; j<arr.length; j++) {
				sum=arr[i]+arr[j];
				if(sum==9) {
					System.out.print("("+arr[i]+","+arr[j]+")");
				}
				else {
					sum=0;
				}
			}
		}

	}

}

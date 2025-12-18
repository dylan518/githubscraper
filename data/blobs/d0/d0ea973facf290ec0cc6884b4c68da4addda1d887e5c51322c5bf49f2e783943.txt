package MergeSort;

import java.util.Arrays;

public class MergeSort {

	/*
	 * Merge sort is a popular and efficient sorting algorithm 
	 * that follows the divide-and-conquer paradigm. 
	 * It breaks down the input array into smaller subarrays, sorts them, 
	 * and then merges them back together to produce the sorted output.
	 * The merge step is the key operation in merge sort. 
	 * It compares the elements from the two subarrays and places 
	 * them in the correct order into a temporary array. 
	 * Finally, the temporary array is copied back to the original array, 
	 * producing the sorted result.
	 */
	
	
	static int[] array = {11,4,7,9,3,1,2,5,6}; // sample array.
	
	public static void sort(int low, int high) {// Low is the starting index of the array, high is the ending index of array
		
		if(low < high) { // Condition check whether there are more than 1 element in the array.
			int mid  = ( low + high )/ 2;

			MergeSort.sort(low, mid);
			MergeSort.sort(mid+1, high);

			MergeSort.merge(low, mid, high);
		}
	}
	
	
	public static void merge(int low, int mid, int high) {
		/*
		 * using Low, Mid, High , we divide the array and 
		 * save the divided array into two temporary array.i.e "ListA" and "ListB"
		 */
		int[] listA= Arrays.copyOfRange(array, low, mid+1);
		int[] listB= Arrays.copyOfRange(array, mid+1, high+1);

		
		int i=0,j=0,k=low; 
		

		while (i < listA.length && j < listB.length) { 
			/* 
			 * comparing the arrays (ListA[] and ListB[]) 
			 * and saving the result in the main array (array[])
			*/
			if(listA[i] < listB[j]) {
				MergeSort.array[k] = listA[i];
				i++;
			} else {
				MergeSort.array[k] = listB[j];
				j++;
			}
			k++;
		}
		

		/*
		 * Adding remaining array elements to the main array[], 
		 * elements which cannot be compare because the length 
		 * of ListA and ListB some times not same length.
		 */
			for(  ; j<listB.length; j++) {
				MergeSort.array[k] = listB[j];
				k++;
			}
			for(  ; i<listA.length; i++) {
				MergeSort.array[k] = listA[i];
				k++;
			}

	}



	
	public static void main(String[] args) {
		MergeSort.sort(0, MergeSort.array.length-1);
		for (int i=0;i<array.length;i++) {
			System.out.print(array[i]+ " , ");
		}
	}

}

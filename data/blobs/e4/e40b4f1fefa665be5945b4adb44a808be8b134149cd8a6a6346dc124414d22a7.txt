import java.util.Arrays;

public class FindCommon {

	public static void main(String[] args) {
		int[] arr1 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		int[] arr2 = {6, 2, 7, 1, 0};
		
		System.out.println(Arrays.toString(findCommon(arr1, arr2)));
	}
	
	public static int[] findCommon(int[] arr1, int[] arr2) {
		int z = 0;
		int[] tempArray = new int[Math.min(arr1.length, arr2.length)];
		for (int i = 0; i < arr1.length; i++) {
			for (int j = 0; j < arr2.length; j++) {
				if (arr1[i] == arr2[j]) {
					tempArray[z] = arr1[i];
					z++;
				}
			}
		}
		int[] finalArray = Arrays.copyOf(tempArray, z);
		return finalArray;
	}

}

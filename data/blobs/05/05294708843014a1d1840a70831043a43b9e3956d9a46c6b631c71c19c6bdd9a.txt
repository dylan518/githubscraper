package aws;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class FourSumNumber {

	public static void main(String[] args) {
		/*
		 * [7, 6, 4, 1, -1, 2] [7, 6, 4, -1],[7, 6, 2, 1]
		 * 
		 * 
		 * 
		 */
		// int[] array = { 7, 6, 4, 1, -1, 2 };
		int[] array = { -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
		int targetSum = 16;
		targetSum = 4;
		int target = 3; // [4, -1],[1, 2]
		int targeter = 8;
		//System.out.println(fourSumNumber(array, targetSum));
		// System.out.println(twoSum(array, target));
	       System.out.println(threeSum(array, targeter));
	}

	static List<Integer[]> fourSumNumber(int[] array, int targetSum) {
		int n = array.length - 1;
		int previous = 0;
		int current = 0;
		int i;
		List<Integer[]> list = new ArrayList<>();
		List<List<Integer>> lister = new ArrayList<>();

		for (i = 1; i <= n; i++) {
			HashMap<Integer, Integer> map = new HashMap<>();
			previous = array[i - 1];
			current = array[i];

			for (int k = i + 1; k <= n; k++) {
				int valueOfK = array[k];
				int sumOf3 = previous + current + valueOfK;
				int difference = targetSum - sumOf3;
				if (map.containsKey(difference)) {
					list.add(new Integer[] { previous, current, valueOfK, difference });
				}
				// map.put(array[k], array[k]);
			}

		}

		list.forEach(a -> {
			System.out.println(Arrays.toString(a));
		});

		return list;

	}

	static List<int[]> twoSum(int[] array, int targetSum) {
		List<int[]> list = new ArrayList<>();
		Map<Integer, Integer> map = new HashMap<>();

		int lookup = 0;
		for (int i = 0; i < array.length; i++) {
			lookup = targetSum - array[i];
			if (map.containsKey(lookup)) {
				list.add(new int[] { lookup, array[i] });
			}
			map.put(array[i], array[i]);
		}
		list.forEach(a -> {
			System.out.println(Arrays.toString(a));
		});
		return list;
	}

	static List<Integer[]> threeSum(int[] array, int targetSum) {
		List<Integer[]> list = new ArrayList<>();
		int n = array.length;

		for (int i = 0; i < n; i++) {
			int left = i;
			int right = n - 1;
			while (left < right) {
				int diff = targetSum - array[i];
				int leftNum = array[left];
				int rightNum = array[right];
				if (leftNum + rightNum == diff) {
					list.add(new Integer[] { array[i], leftNum, array[right] });
					left++;
					right++;
				} else if (leftNum + rightNum < diff) {
					left++;
				} else {
					right++;
				}
			}
		}
		list.forEach(a -> {
			System.out.println(a);
		});

		return new ArrayList<Integer[]>();
	}

}

package Arrays;

import java.util.Arrays;

public class Dutch_National_Flag_algorithm {

	public static void main(String[] args) {
		int[] number = { 2, 1, 0, 0, 1, 2 };

		int count1 = 0;
		int count2 = 0;
		int count3 = 0;

		for (int num : number) {
			if (num == 0) {
				count1++;
			} else if (num == 1) {
				count2++;
			} else {
				count3++;
			}
		}

		int i = 0;
		while (count1 > 0) {
			number[i++] = 0;
			count1--;
		}
		while (count2 > 0) {

			number[i++] = 1;
			count2--;
		}
		while (count3 > 0) {
			number[i++] = 2;
			count3--;
		}
		System.out.println(Arrays.toString(number));
	}
}

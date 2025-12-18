

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class BOJ_1181_단어정렬_정유준 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] arr = new String[N];

		for (int i = 0; i < arr.length; i++) {
			arr[i] = sc.next();
		}

		Arrays.sort(arr, new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				if (o1.length() == o2.length()) {
					return o1.compareTo(o2);
				}
				return o1.length() - o2.length();
			}
		});
		String[] answer = Arrays.stream(arr).distinct().toArray(String[]::new);
		for (int i = 0; i < answer.length; i++) {
			System.out.println(answer[i]);
		}
	}
}

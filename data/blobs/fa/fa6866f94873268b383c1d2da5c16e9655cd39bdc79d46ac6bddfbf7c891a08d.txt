package src;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class 전광판 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		Map<Character, String> lights = new HashMap<>();
		lights.put('0', "1110111");
		lights.put('1', "0010010");
		lights.put('2', "1011101");
		lights.put('3', "1011011");
		lights.put('4', "0111010");
		lights.put('5', "1101011");
		lights.put('6', "1101111");
		lights.put('7', "1110010");
		lights.put('8', "1111111");
		lights.put('9', "1111011");
		lights.put(' ', "0000000");

		int[][] nums = new int[t][2];
		for (int i = 0; i < t; i++) {
			String[] split = br.readLine().split(" ");

			nums[i][0] = Integer.parseInt(split[0]);
			nums[i][1] = Integer.parseInt(split[1]);
		}

		for (int i = 0; i < t; i++) {
			int cnt = 0;

			char[] d1 = String.format("%5s", nums[i][0]).toCharArray();
			char[] d2 = String.format("%5s", nums[i][1]).toCharArray();

			for (int j = 0; j < 5; j++) {
				cnt += solution(lights.get(d1[j]), lights.get(d2[j]));
			}
			System.out.println(cnt);
		}
	}

	private static int solution(String d1, String d2) {
		int cnt = 0;
		char[] ca = d1.toCharArray();
		char[] cb = d2.toCharArray();

		for (int i = 0; i < ca.length; i++) {
			if (ca[i] != cb[i]) {
				cnt++;
			}
		}
		return cnt;
	}
}

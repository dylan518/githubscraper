package Algorithm;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main5565 {  // 영수증

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int sum = Integer.parseInt(br.readLine());
		for (int i = 0; i < 9; i++) {
			sum -= Integer.parseInt(br.readLine());
		}
		
		System.out.println(sum);
	}

}

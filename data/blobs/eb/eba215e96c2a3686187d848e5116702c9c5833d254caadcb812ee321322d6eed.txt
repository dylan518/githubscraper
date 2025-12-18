package stage13;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Step_6 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String n = br.readLine();
		br.close();
		String[] strArr = n.split("");

		Arrays.sort(strArr);
		for (int i = 0; i < n.length(); i++) {
			bw.write(strArr[n.length() - 1 - i]);
		}
		bw.write("\n");
		bw.flush();
		bw.close();
	}
}

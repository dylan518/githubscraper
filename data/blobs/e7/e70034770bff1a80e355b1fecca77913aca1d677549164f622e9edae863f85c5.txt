package exam;

import java.util.Random;

public class Quest125 {
	public static void main(String[] args) {
		String alphabet = "abcdefghijklmnopqrstuvwxyz";
		Random r = new Random();
		System.out.println(alphabet.charAt(r.nextInt(26) + 1));
	}
}

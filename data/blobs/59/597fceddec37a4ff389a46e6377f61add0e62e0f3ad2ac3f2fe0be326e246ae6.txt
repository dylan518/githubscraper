import java.util.Scanner;
import java.lang.Math;

public class Janitor{
	public static void main(String[] args){
		Scanner s = new Scanner(System.in);
		int[] sides = java.util.Arrays.stream(s.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		double sp = java.util.Arrays.stream(sides).sum() / 2.0;
		double res = 1;
		for (int side : sides) {
			res *= sp - side;
		}
		res = Math.sqrt(res);
		System.out.println(Double.toString(res));
	}
}

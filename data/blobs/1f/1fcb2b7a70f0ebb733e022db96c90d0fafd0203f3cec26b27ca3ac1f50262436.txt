package pro08;

public class Code07_Knapsack {

	public static int maxValue1(int[] weights, int[] values, int bag) {
		return process1(weights, values, 0, 0, bag);
	}
	//w[index] 当前货物的重量
	//v[index] 当前货物的重量
	//index 当前货物号
	//alreweight 目前重量
	//bag 袋子总重量
	public static int process1(int[] weights, int[] values, int i, int alreadyweight, int bag) {
		//重量超重
		if (alreadyweight > bag) {
			return 0;
		}

		if (i == weights.length) {
			return 0;
		}

		return Math.max(

				process1(weights, values, i + 1, alreadyweight, bag),//不要index货物，获得的最大价值

				values[i] + process1(weights, values, i + 1, alreadyweight + weights[i], bag));//要index货物，获得的最大价值
	}

	public static int maxValue2(int[] c, int[] p, int bag) {
		int[][] dp = new int[c.length + 1][bag + 1];
		for (int i = c.length - 1; i >= 0; i--) {
			for (int j = bag; j >= 0; j--) {
				dp[i][j] = dp[i + 1][j];
				if (j + c[i] <= bag) {
					dp[i][j] = Math.max(dp[i][j], p[i] + dp[i + 1][j + c[i]]);
				}
			}
		}
		return dp[0][0];
	}

	public static void main(String[] args) {
		int[] weights = { 3, 2, 4, 7 };
		int[] values = { 5, 6, 3, 19 };
		int bag = 11;
		System.out.println(maxValue1(weights, values, bag));
		System.out.println(maxValue2(weights, values, bag));
	}

}

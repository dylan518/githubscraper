package 수현.다이나믹_프로그래밍;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 동물원 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] dp = new long[N + 1];

        if(N == 1){
            System.out.println(3);
            System.exit(0);
        }

        dp[1] = 3;
        dp[2] = 7;

        for (int i = 3; i <= N; i++) {
            dp[i] = (dp[i - 2] + dp[i - 1] * 2) % 9901;
        }

        System.out.println(dp[N]);
    }
}

package Ex1904;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] arrData;
    static int max = 1000001;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int input = Integer.parseInt(br.readLine());
        arrData = new int[max];
        System.out.println(dp(input));
    }

    public static int dp(int N) {
        arrData[1] = 1;
        arrData[2] = 2;

        for(int i = 3; i <= N; i++) {
            arrData[i] = (arrData[i-2] + arrData[i-1]) % 15746;
        }
        return arrData[N];
    }
}

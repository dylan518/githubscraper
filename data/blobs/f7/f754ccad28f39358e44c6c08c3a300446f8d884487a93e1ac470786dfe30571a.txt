package baekjoon.baekjoon19XXX;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Exercise19751 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] num = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(num);

        int temp = num[1];
        num[1] = num[2];
        num[2] = temp;
        Arrays.stream(num).forEach(value -> System.out.print(value + " "));
    }
}

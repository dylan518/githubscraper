package baekjoon;

import java.io.*;
import java.util.*;

public class _15657 {
    static int n, m;
    static int[] valueArr, trackArr;

    public static void main(String[] args) throws IOException {
        int depth = 0;
        int start = 0;
        init();

        String result = track(depth, start);

        System.out.print(result);
    }

    public static String track(int depth, int start) {
        StringBuilder sb = new StringBuilder();

        if (depth < m) {
            for (int i = start; i < n; i++) {
                trackArr[depth] = valueArr[i];
                sb.append(track(depth + 1, i));
            }
        } else {
            for (int i = 0; i < m; i++) {
                sb.append(trackArr[i]).append(" ");
            }
            sb.append("\n");
        }

        return sb.toString();
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        valueArr = new int[n];
        for (int i = 0; i < n; i++) {
            valueArr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(valueArr);

        trackArr = new int[m];
    }
}

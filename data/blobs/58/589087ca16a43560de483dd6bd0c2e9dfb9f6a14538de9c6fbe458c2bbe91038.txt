package day1;

import java.util.*;
import java.io.*;

public class B1260 {
        public  static int n, len, start, cnt_dfs = 0, cnt_bfs = 0;
        public static int[][] arr;
        public static boolean[] dfs, bfs;
        public static int answer = 0;
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            len = Integer.parseInt(st.nextToken());
            start = Integer.parseInt(st.nextToken());

            arr = new int[n + 1][n + 1];
            dfs = new boolean[n + 1];
            bfs = new boolean[n + 1];

            for (int i = 0; i <= n; i++) {
                dfs[i] = false;
                bfs[i] = false;
                for (int j = 0; j <= n; j++) {
                    arr[i][j] = 0;
                }
            }

            for (int i = 0; i < len; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                arr[x][y] = 1;
                arr[y][x] = 1;
            }

            dfs(start);
            System.out.println();
            bfs(start);
        }

        public static void dfs(int start) {
            dfs[start] = true;
            cnt_dfs++;
            if (cnt_dfs == n)
                System.out.print(start);
            else
                System.out.print(start + " ");
            for (int i = 1; i <= n; i++) {
                if (arr[start][i] == 1 && !dfs[i]) {
//                System.out.println("i = " + i);
                    dfs[i] = true;
                    dfs(i);
                }
            }
        }

        public static void bfs(int start) {
            Queue<Integer> q = new LinkedList<>();
            q.add(start);
            bfs[start] = true;

            while (!q.isEmpty()) {
                int x = q.poll();
                cnt_bfs++;
                if (cnt_bfs == n)
                    System.out.print(x);
                else
                    System.out.print(x + " ");
                for (int i = 1; i <= n; i++) {
                    if (arr[x][i] == 1 && !bfs[i]) {
                        q.add(i);
                        bfs[i] = true;
                    }
                }
            }

    }
}

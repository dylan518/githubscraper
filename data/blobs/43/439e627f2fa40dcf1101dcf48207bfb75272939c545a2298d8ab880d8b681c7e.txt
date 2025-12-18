package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ1987 {
    static class node {
        int x;
        int y;
        String[] way;
        int count;

        public node(int x, int y, String[] way, int count) {
            this.x = x;
            this.y = y;
            this.way = way;
            this.count = count;
        }
    }

    static int[] moveX = {1, 0, -1, 0};
    static int[] moveY = {0, -1, 0, 1};
    static int maxCount = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        char[][] map = new char[R][C];

        for (int i = 0; i < R; i++) {
            String s = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = s.charAt(j);
            }
        }

        Queue<node> queue = new ArrayDeque<>();
        String[] initialWay = new String[] {String.valueOf(map[0][0])};
        queue.add(new node(0, 0, initialWay, 1));

        while (!queue.isEmpty()) {
            node current = queue.poll();
            int x = current.x;
            int y = current.y;
            String[] way = current.way;
            int count = current.count;

            if (count > maxCount) maxCount = count;

            for (int i = 0; i < 4; i++) {
                int nextX = x + moveX[i];
                int nextY = y + moveY[i];
                if (nextX < 0 || nextX >= R || nextY < 0 || nextY >= C) continue;

                boolean alreadyVisited = Arrays.stream(way)
                        .anyMatch(ch -> ch.equals(String.valueOf(map[nextX][nextY])));
                if (alreadyVisited) continue;

                String[] newWay = Arrays.copyOf(way, way.length + 1);
                newWay[newWay.length - 1] = String.valueOf(map[nextX][nextY]);
                queue.add(new node(nextX, nextY, newWay, count + 1));
            }
        }

        System.out.println(maxCount);
    }
}

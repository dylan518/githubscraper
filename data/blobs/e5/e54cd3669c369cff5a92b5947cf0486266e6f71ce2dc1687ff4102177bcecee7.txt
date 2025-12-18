package DFS;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Rank {
//    static int[] visited;
    public int solution(int n, int[][] results) {
        int[][] visited = new int[n + 1][n + 1];

        for (int[] result : results) {
            int winner = result[0];
            int loser = result[1];
            visited[winner][loser] = 1;
            visited[loser][winner] = -1;
        }
        return floydWashall(n, visited);
    }

    public static int floydWashall(int n, int[][] visited) {
        int answer = 0;

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (visited[i][k] == 1 && visited[k][j] == 1) {
                        visited[i][j] = 1;
                    }
                    if (visited[i][k] == -1 && visited[k][j] == -1) {
                        visited[i][j] = -1;
                    }
                }
            }
        }

        return getCount(visited);
    }

    public static int getCount(int[][] visited) {
        int answer = 0;

        for (int i = 1; i < visited.length; i++){
            int count = 0;
            for (int j = 1; j < visited.length; j++) {
                if (visited[i][j] != 0 || i == j) count++;
            }

            if (count == visited.length - 1) answer++;
        }

        return answer;
    }

//    public static void bfs(int start, ArrayList<Integer>[] graph) {
//        Queue<Integer> queue = new LinkedList<>();
//        queue.offer(start);
//        if (visited[start] == 0) {
//            visited[start] = 1;
//        }
//
//        while (!queue.isEmpty()) {
//            int cur = queue.poll();
//            for (int next : graph[cur]) {
//                if (visited[next] < visited[cur]) {
//                    visited[next] += visited[cur];
//                    queue.offer(next);
//                }
//            }
//        }
//
//    }
//
//    public static int getCount() {
//        int result = 0;
//        for (int i : visited) {
//            if (visited.length == i) {
//                result++;
//            }
//            System.out.println(i);
//        }
//        return result;
//    }

    public static void main(String[] args) {
        int[][] results = {
                {4, 3}, {4, 2}, {3, 2}, {1, 2}, {2, 5}
        };

        int n = 5;

        Rank rank = new Rank();
        System.out.println(rank.solution(n, results));
    }
}

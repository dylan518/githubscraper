package site.inflearn.DFS_BFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 섬나라_아일랜드 {
    static int[] dx = {1, 1, 0, 0, -1, -1, -1, 1};
    static int[] dy = {0, 1, 1, -1, 1, 0, -1, -1};
    static boolean[][] visited;
    static int[][] board;
    static int row;
    static int col;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        row = col = N;
        board = new int[col][row];
        visited = new boolean[col][row];

        for (int i = 0; i < col; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < row; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        searchMap();
        System.out.println(answer);
    }

    private static void searchMap() {
        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (board[i][j] == 1 && !visited[i][j]) {
                    answer++;
                    visited[i][j] = true;
                    DFS(i, j);
                }
            }
        }
    }

    private static void DFS(int startX, int startY) {
        for (int i = 0; i < 8; i++) {
            int nx = startX + dx[i];
            int ny = startY + dy[i];

            if (nx >= 0 && nx < col && ny >= 0 && ny < row && board[nx][ny] == 1) {
                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    DFS(nx, ny);
                }
            }
        }
    }
}

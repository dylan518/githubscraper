import java.io.*;
import java.util.*;

public class Graph input_adjacent array {
    // Enter a directed graph with N vertices and M edges
    public static void main(String[] args) throws Exception{
        // BufferedReader 선언 및 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer 선언
        StringTokenizer st;
        // Number of test cases in the first line T
        int T = Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++)
        {
            // First line of each case, number of vertices N, number of trunk lines M
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            // Create adjacency array
            int adjMat[][] = new int[N+1][N+1];

            for(int i = 1; i <= N; i++)
            {
                for(int j = 1; j <= N; j++)
                {
                    // Initial value to indicate that the trunk is not connected
                    adjMat[i][j] = -1;
                }
            }

            for(int i = 0; i < M; i++)
            {
                // Information input of each trunk from vertex, to vertex, cost
                st = new StringTokenizer(br.readLine());
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                int cost = Integer.parseInt(st.nextToken());
                adjMat[from][to] = cost;
            }
        }
    }
}
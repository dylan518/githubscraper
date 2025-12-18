package graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class N2644 {
	
	static int p1;
	static int p2;
	
	static int N;
	static int[] dist;
	static int[][] map;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		dist = new int[N + 1];
		map = new int[N + 1][N + 1];
		
		st = new StringTokenizer(br.readLine());
		p1 = Integer.parseInt(st.nextToken());
		p2 = Integer.parseInt(st.nextToken());
		
		int M = Integer.parseInt(br.readLine());
		while (M-- > 0) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			map[x][y] = map[y][x] = 1;
		}
		
		System.out.println(bfs(p1, p2));
		
		Arrays.fill(dist, 0);
		
		dfs(p1, p2);
		System.out.println(dist[p2]);
	}
	
	static int bfs(int start, int end) {
		Queue<Integer> q = new LinkedList<>();
		q.offer(start);
		
		while (!q.isEmpty()) {
			int v = q.poll();
			
			if (v == end) {
				return dist[v];
			}
			
			for (int i = 1; i <= N; i++) {
				if (map[v][i] == 1 && dist[i] == 0) {
					dist[i] = dist[v] + 1;
					q.offer(i);
				}
			}
		}
		
		return -1;
	}
	
	static void dfs(int start, int end) {
		if (start == end) return;
		
		for (int i = 1; i <= N; i++) {
			if (map[start][i] == 1 && dist[i] == 0) {
				dist[i] = dist[start] + 1;
				dfs(i, end);
			}
		}
	}
	
}

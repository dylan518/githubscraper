package codingtest.baekjoon.BFS_DFS;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class 트리의부모찾기 {

	private static List<Integer>[] list;	//트리 연결 정보
	private static int[] parents;			//부모 노드 저장 배열
	private static boolean[] visited;		//방문 여부 체크 배열
	
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	//첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
    	int N = sc.nextInt();
    	
    	list 	= new ArrayList[N+1];		//트리 연결 정보 초기화
    	parents	= new int[N+1];				//부모 노드 저장 배열 초기화
    	visited	= new boolean[N+1];			//방문 여부 체크 배열 초기화
    	
    	//트리 연결 정보 배열 내 리스트 초기화
    	for(int a = 0 ; a < list.length ; a++) list[a] = new ArrayList<Integer>();
    	
    	//둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
    	//노드별 간선 연결
    	for(int a = 0 ; a < N - 1; a++) {
    		int x = sc.nextInt();
    		int y = sc.nextInt();
    		list[x].add(y);
    		list[y].add(x);
    	}//end for()
    	
    	//부모 노드 탐색 + 루트부터
    	dfs(1);
    	
    	//결과 출력
    	for(int a = 2 ; a < parents.length ; a++) System.out.println(parents[a]);
    }//end main()

	private static void dfs(int i) {
		if(visited[i]) return;
		
		//방문 여부 체크
		visited[i] = true;
		
		//list foreach
		//i노드에 연결된 정보 반복
		for(int num : list[i]) {
			//연결 정보가 탐색된 곳이 아니라면
			if(!visited[num]) {
				parents[num] = i;
				dfs(num);
			}//end if()
		}//end for()
		
	}//end dfs()

}//end class()
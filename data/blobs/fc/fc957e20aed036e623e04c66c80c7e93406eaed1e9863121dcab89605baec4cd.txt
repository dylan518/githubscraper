package org.jsjeong.algorithm.routing.bfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * 1번 정점에서 각 정점으로 가는 최소 간선수를 2번 정점부터 차례대로 출력하세요.
 *
 */
public class BFS1 {

    static int[] ch, dis;

    public static void solution(int[][] arr) {
        List<List<Integer>> graph = new ArrayList<>();

        for(int i=0; i<=6; i++){
            graph.add(new ArrayList<>());
        }

        for (int[] e : arr) {
            graph.get(e[0]).add(e[1]);
        }

        ch = new int[graph.size()];
        dis = new int[graph.size()];

        bfs(graph, 1);

        for(int i=2; i<dis.length; i++){
            System.out.println(i+" : "+dis[i]);
        }
    }

    public static void bfs(List<List<Integer>> graph, int v) {
        ch[v]=1;
        dis[v]=0;
        Queue<Integer> queue=new LinkedList<>();
        queue.offer(v);
        while(!queue.isEmpty()){
            int cv=queue.poll();
            for(int nv : graph.get(cv)){
                if(ch[nv]==0){
                    ch[nv]=1;
                    queue.offer(nv);
                    dis[nv]=dis[cv]+1;
                }
            }
        }
    }


    public static void main(String[] args) {
        int[][] arr = {{1,3}, {1,4}, {2,1}, {2,5}, {3,4}, {4,5}, {4,6}, {6,2}, {6,5}};
        solution(arr);
    }
}

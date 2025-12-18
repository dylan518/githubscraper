

import java.util.*;
class minWireRequired {

    static class Edge implements Comparable<Edge> {
        int src;
        int nbr;
        int wt;

        Edge(int src, int nbr, int wt) {
            this.src = src;
            this.nbr = nbr;
            this.wt = wt;
        }

        public int compareTo(Edge o) {
            return this.wt - o.wt;
        }
    }

    static int parent[];
    static int rank[];
    public static void Krushkal(ArrayList<Edge>[] graph) {

        PriorityQueue<Edge> pq = new PriorityQueue<>();

        for (int v = 0; v < graph.length; v++) {
            for (Edge e : graph[v]) {
                pq.add(e);
            }
        }

        parent = new int[graph.length];
        rank = new int[graph.length];

        for(int i = 0; i < graph.length; i++){
            parent[i] = i;
            rank[i] = i;
        }

        while(pq.size() > 0){
            Edge rem = pq.remove();

            int srclead = find(rem.src);
            int nbrlead = find(rem.nbr);

            if(srclead != nbrlead){
                System.out.println(rem.src + " - " + rem.nbr + " @ " + rem.wt);

                union(srclead, nbrlead);
            }
        }
    }

    public static int find(int x){
        if(parent[x] == x){
            return x;
        }else{
            parent[x] = find(parent[x]);
            return parent[x];
        }
    }

    public static void union(int s1l, int s2l){
        if(rank[s1l] < rank[s2l]){
            parent[s1l] = s2l;
        }else if(rank[s2l] < rank[s1l]){
            parent[s2l] = s1l;
        }else{
            parent[s1l] = s2l;
            rank[s2l]++;
        }
    }
}
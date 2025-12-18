package level2.leetCodePathWithMaximumProbability;

import java.util.*;

public class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        // 그래프 구성
        List<List<Pair>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0], v = edges[i][1];
            double p = succProb[i];
            graph.get(u).add(new Pair(v, p));
            graph.get(v).add(new Pair(u, p));
        }

        // Dijkstra 알고리즘
        double[] maxProb = new double[n];
        maxProb[start] = 1.0;

        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> Double.compare(b.prob, a.prob));
        pq.offer(new Pair(start, 1.0));

        while (!pq.isEmpty()) {
            Pair current = pq.poll();
            int node = current.node;
            double prob = current.prob;

            if (node == end) return prob;

            if (prob < maxProb[node]) continue;

            for (Pair next : graph.get(node)) {
                double newProb = prob * next.prob;
                if (newProb > maxProb[next.node]) {
                    maxProb[next.node] = newProb;
                    pq.offer(new Pair(next.node, newProb));
                }
            }
        }

        return 0.0;
    }

    class Pair {
        int node;
        double prob;

        Pair(int node, double prob) {
            this.node = node;
            this.prob = prob;
        }
    }
}

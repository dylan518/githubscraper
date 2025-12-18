package Graph;

import java.util.ArrayList;

public class RepersentationOfGraph {
    public static int[][] printAdjacency(int n, int m, int[][] edges) {
        ArrayList<ArrayList<Integer>> list=new ArrayList<>();
        for(int i=0;i<n;i++){
            list.add(new ArrayList<>());
        }
        for(int i=0;i<m;i++){
            int j=edges[i][0];
            int k=edges[i][1];
            list.get(j).add(k); 
            list.get(k).add(j);

        }
        int matrix[][] = new int[n][];

        for (int i = 0; i < n; i++) {
            ArrayList<Integer> node = new ArrayList<>();
            node.add(i); 
            node.addAll(list.get(i));
            matrix[i] = new int[node.size()];
            for (int j = 0; j < node.size(); j++) {
                matrix[i][j] = node.get(j);
            }
        }
        return matrix;
    }
}

package leetcode.graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class CourseSchedule {
    public static void main(String[] args) {
    	int[][] prerequisites = {
    		{0,1},
    		{1,3},
    		{1,4},
    		{1,2},
    		{2,3}
    	};
    	canFinish(5,prerequisites);
    }
    
    public static boolean canFinish(int numCourses, int[][] prerequisites) {
        int n = prerequisites.length;
        HashMap<Integer, List<Integer>> hmp = new HashMap<>();
        int[] visited = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();
        int count = 0;
        for(int i = 0; i<n; i++) {
            List<Integer> lst = hmp.getOrDefault(prerequisites[i][0],new ArrayList<Integer>());
            lst.add(prerequisites[i][1]);
            hmp.put(prerequisites[i][0], lst);
            visited[prerequisites[i][1]]++;
        }
        for(int i = 0; i<numCourses; i++){
            if(visited[i]==0)
                queue.offer(i);
        }
        while(!queue.isEmpty()) {
            int idx = queue.poll();
            count++;
            for(Integer val : hmp.getOrDefault(idx,new ArrayList<Integer>())){
            visited[val] --;
                if(visited[val]==0)
                	
                	queue.offer(val); 
                
            }
        }
         return count == numCourses;
    }
}

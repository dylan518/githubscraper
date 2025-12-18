class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        Queue<int[]> q=new LinkedList<>();
        List<Integer> al[]=new ArrayList[n];
        for(int i=0;i<n;i++)
            al[i]=new ArrayList<>();
        for(int i=0;i<n;i++)
        {
            if(manager[i]!=-1)
                al[manager[i]].add(i);
        }
        q.add(new int[]{headID,0});
        int max=Integer.MIN_VALUE;
        while(!q.isEmpty())
        {
            int ans[]=q.poll();
            int u=ans[0];
            int v=ans[1];
            max=Math.max(max,v);
            for(int i:al[u])
            {
                q.add(new int[]{i,v+informTime[u]});
            }
        }
        return max;
    }
}
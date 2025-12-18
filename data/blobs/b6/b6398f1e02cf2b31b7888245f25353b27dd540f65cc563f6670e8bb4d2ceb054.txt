class Solution {
    public int orangesRotting(int[][] grid) {
        int fresh = 0,rotten =0;
        Queue<int[]> q = new LinkedList<>();
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]==1)fresh++;
                if(grid[i][j]==2){
                    q.offer(new int[]{i,j});
                    rotten++;
                }
            }
        }
        if(rotten==0 && fresh==0) return 0;
        int time =0;
        int[]dRow = new int[]{0,0,1,-1};
        int[]dCol = new int[]{1,-1,0,0};
        while(!q.isEmpty()){
            int s = q.size();
            for(int i = 0; i<s; i++){
                int[]top = q.poll();
                int row = top[0];
                int col = top[1];
                for(int k=0;k<4;k++){
                    int nRow = row + dRow[k];
                    int nCol = col + dCol[k];
                    if(nRow>=0 && nCol>=0 && nRow<grid.length && nCol<grid[0].length && grid[nRow][nCol]==1){
                        grid[nRow][nCol]=2;
                        fresh--;
                        q.offer(new int[]{nRow,nCol});
                    }
                }
            }
            time++; 
        }
        if(fresh!=0)return -1;
        
        return time-1;//because while loop runs one extra time when all the oranges are rotten
    }
}
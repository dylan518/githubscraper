class Solution {
boolean isSame = true;
boolean topLevel = true;
public int countSubIslands(int[][] grid1, int[][] grid2) {
int m = grid1.length;
int n = grid1[0].length;

    int[] parent = new int[m*n];
    int[] rank = new int[m*n];
    
    for (int i=0; i<m*n; i++) {
        parent[i] = i;
        rank[i] = 1;
    }
    
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            if (grid1[i][j] == 1) {
                int first = i*n + j;
                recursion(i, j, m, n, grid1, first, parent, rank, false);
                
            }
        }
    }
    int count = 0;
    
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            if (grid2[i][j] == 1 && grid1[i][j] == -1) {
                isSame = true;
                topLevel = true;
                int first = i*n + j;
                recursion(i, j, m, n, grid2, first, parent, rank, true);
                if (topLevel) {
                    count++;
                }
                
            }
        }
    }
    
    return count;
    
}

public boolean isSafe(int x, int y, int m, int n) {
    return (x >= 0 && x < m && y >= 0 && y < n);
}


public void recursion(int x, int y, int m, int n, int[][] grid, int first, int[] parent, int[] rank, boolean isGrid2) {
    if (isSafe(x, y, m, n) && grid[x][y] == 1) {
        
        int second = x*n + y;
        grid[x][y] = -1;
        
        if (first != second || isGrid2) {
            union(first, second, parent, rank);
        }
        
        if (isGrid2 && !isSame) {
            topLevel = false;
        }
        
        recursion(x-1, y, m, n, grid, first, parent, rank, isGrid2);
        recursion(x+1, y, m, n, grid, first, parent, rank, isGrid2);
        recursion(x, y+1, m, n, grid, first, parent, rank, isGrid2);
        recursion(x, y-1, m, n, grid, first, parent, rank, isGrid2);
        
        
    }
}


public int find(int x, int[] parent) {
    if (parent[x] == x) {
        return x;
    }
    int temp = find(parent[x], parent);
    parent[x] = temp;
    
    return temp;
}

public void union(int x, int y, int[] parent, int[] rank) {
    int lx = find(x, parent);
    int ly = find(y, parent);
    
    if (lx != ly) {
        if (rank[lx] > rank[ly]) {
            parent[ly] = lx;
        }
        else if (rank[ly] > rank[lx]) {
            parent[lx] = ly;
        }
        else {
            parent[ly] = lx;
            rank[lx]++;
        }
        isSame = false;
    }
    else {
        isSame = true;
    }
}
}
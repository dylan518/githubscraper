// { Driver Code Starts
// Initial Template for Java

import java.util.*;
class Rat {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int[][] a = new int[n][n];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) a[i][j] = sc.nextInt();

            Solution obj = new Solution();
            ArrayList<String> res = obj.findPath(a, n);
            Collections.sort(res);
            if (res.size() > 0) {
                for (int i = 0; i < res.size(); i++)
                    System.out.print(res.get(i) + " ");
                System.out.println();
            } else {
                System.out.println(-1);
            }
        }
    }
}
// } Driver Code Ends


// User function Template for Java

// m is the given matrix and n is the order of matrix
class Solution {
   static ArrayList<String> ans = new ArrayList<>();
    public static ArrayList<String> findPath(int[][] m, int n) {
        // Your code here
        ans.clear();
        
        if(m[n-1][n-1]==0||m[0][0]==0) return ans;
        helper("",m,0,0,n);
        return ans;
    }
    static void helper(String s,int[][]m,int row,int col,int n){
        if(row==n-1&& col==n-1){
            ans.add(s);
            return;
        }
        if(m[row][col]==0) return;
        
        m[row][col] = 0;
        
        if(row<n-1){
            helper(s+'D',m,row+1,col,n);
        }
        if(col<n-1){
            helper(s+'R',m,row,col+1,n);
        }
        if(row>0){
            helper(s+'U',m,row-1,col,n);
        }
        if(col>0){
            helper(s+'L',m,row,col-1,n);
        }
        m[row][col] = 1;
    }
}
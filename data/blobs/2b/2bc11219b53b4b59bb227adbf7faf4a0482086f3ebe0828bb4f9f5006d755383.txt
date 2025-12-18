import java.util.Arrays;

public class MinCosttoFillGivenWeightinaBag {
    public int solve(int cost[], int n,int w, int [][] dp){
        if(n==-1 && w==0){
            return 0;
        }
        if(n==-1){
            return Integer.MAX_VALUE;
        }
        if(w==0){
            return 0;
        }
        if(dp[n][w]!=-1){
            return dp[n][w];
        }
        if(n+1>w || cost[n]==-1){
            return dp[n][w] = solve(cost , n-1, w, dp);
        }
        
            int excl = solve(cost , n-1, w, dp);
            int incl = cost[n] + solve(cost , n, w-(n+1), dp);
            int ans = Math.min(excl , incl);
            return dp[n][w] = ans;
        
    }
	public int minimumCost(int cost[], int N,int W)
	{
	    int[][]dp = new int[N+1][W+1];
	    for(int[] arr:dp){
	        Arrays.fill(arr, -1);
	    }
		int x = solve(cost , N-1 ,W, dp);
		if(x>Integer.MAX_VALUE){
		    return -1;
		}
		return x;
	}
}

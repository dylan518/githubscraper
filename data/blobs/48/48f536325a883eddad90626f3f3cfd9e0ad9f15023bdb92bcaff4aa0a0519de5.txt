// 1575. Count All Possible Routes
package Hard;
import java.util.Arrays;

public class Hard_1575_Count_All_Possible_Routes {
    // Recursion + Memoization -> TC & SC -> O(n * fuel)
    private static final int MOD = (int) 1E9 + 7;

    public static int countRoutes(int[] locations, int start, int finish, int fuel) {
        int n = locations.length;
        int[][] dp = new int[n+1][fuel+1];
        for (int[] d : dp) Arrays.fill(d, -1);

        return solve(dp, locations, start, finish, fuel, n) % MOD;
    }
    private static int solve(int[][] dp, int[] locations, int currIdx, int destination, int fuel, int n) {
        if (fuel < 0) return 0; // fuel cannot be zero

        if (dp[currIdx][fuel] != -1) return dp[currIdx][fuel];

        int answer = 0;
        if (currIdx == destination) // reached the destination
            answer = 1; // one route found

        for (int i=0; i<n; i++) {
            if (i != currIdx) { // allowed to visit any city more than once
                int availableFuel = fuel - Math.abs(locations[i] - locations[currIdx]);
                answer = (answer + solve(dp, locations, i, destination, availableFuel, n)) % MOD;
            }
        }
        return dp[currIdx][fuel] = answer % MOD;
    }
    public static void main(String[] args) {
        System.out.println(countRoutes(new int[]{2,3,6,8,4},1,3,5));
        System.out.println(countRoutes(new int[]{4,3,1},1,0,6));
        System.out.println(countRoutes(new int[]{5,2,1},0,2,3));
    }
}

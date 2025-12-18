package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class Num216 {

    static class Solution {
        public List<List<Integer>> combinationSum3(int k, int n) {
            List<List<Integer>> ans = new ArrayList<>();
            List<Integer> path = new ArrayList<>();

            dfs(1, k, n, 0,path, ans);
            return ans;
        }

        public void dfs(int begin, int k, int n, int sum, List<Integer> path, List<List<Integer>> ans){
            if(k==0 && sum==n){
                ans.add(new ArrayList<>(path));
                return;
            }
            if(k<0 || begin>9 || (sum>=n && k>0) || (10-begin<k))
                return;


            //不选该数
            dfs(begin+1, k, n, sum, path, ans);

            //选该数
            path.add(begin);
            dfs(begin+1, k-1, n, sum+begin, path, ans);
            path.remove(path.size()-1);
        }
    }

    public static void main(String[] args) {
        int k = 3;
        int n = 9;
        Solution solution = new Solution();
        System.out.println(solution.combinationSum3(k, n));
    }
}

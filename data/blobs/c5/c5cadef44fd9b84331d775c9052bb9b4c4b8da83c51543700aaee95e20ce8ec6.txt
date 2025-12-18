package com.leetcode.problem.arrays;

/**
 * <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/">Problem description</a>
 */
public class Solved_Problem121BestTimeToBuyAndSellStock {

  public static void main(String[] args) {
    System.out.println(new Solution().maxProfit(new int[] {7,1,5,3,6,4})); // 5
    System.out.println(new Solution().maxProfit(new int[] {7,6,4,3,1})); // 0
    System.out.println(new Solution().maxProfit(new int[] {1,2})); // 1
  }

  static class Solution {
    public int maxProfit(int[] prices) {
      if (prices.length < 2) {
        return 0;
      }

      int min = prices[0], max = 0;

      for (int i = 1; i < prices.length; i++) {
        max = Math.max(max, prices[i] - min);
        min = Math.min(min, prices[i]);
      }

      return max;
    }
  }

}

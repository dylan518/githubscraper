public class BestTime {
    //LC121
    public int maxProfit(int[] prices) {
        int min = prices[0];
        int maxProfit = 0;
        int day = 0;
        for (int i = 1; i < prices.length; i++) {
            int localProfit = prices[i] - min;
            if (localProfit > maxProfit) {
                maxProfit = localProfit;
                day = i + 1;
            }
            min = Math.min(prices[i], min);
        }
        return day;
    }
}

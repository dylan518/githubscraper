package com.ds.divideAndConquer;

import java.util.AbstractMap;
import java.util.Map;

/**
 * Find Mid
 * 1. BuyDate and SellDate both are left side of mid
 * 2. BuyDate and SellDate both are right side of mid
 * 3. BuyDate is in the left side and SellDate in the right side of mid
 */
public class StockStrategy {

    // post order traversal
    private Map.Entry<Integer, Integer> findStockStrategy(int[] arr, int left, int right) {
        if (right >= left) {
            return null;
        }
        int mid = left + (right - left) / 2;
        Map.Entry<Integer, Integer> leftStat = findStockStrategy(arr, left, mid);
        Map.Entry<Integer, Integer> rightStat = findStockStrategy(arr, mid + 1, right);
        if (leftStat == null || rightStat == null) {
            return leftStat == null ? rightStat : leftStat;
        }
        int leftProfit = arr[leftStat.getKey()] - arr[leftStat.getValue()];
        int rightProfit = arr[rightStat.getKey()] - arr[rightStat.getValue()];
        int midProfit = arr[leftStat.getKey()] - arr[rightStat.getValue()];

        int maxProfit = Math.max(Math.max(leftProfit, rightProfit), midProfit);

        return maxProfit == leftProfit ? leftStat : maxProfit == rightProfit ? rightStat :
                new AbstractMap.SimpleEntry<>(leftStat.getKey(), rightStat.getValue());
    }
}

package com.ex.gif.strategy;

public class SimpleSumStrategy implements SumStrategy {
    @Override
    public int get(int n) {
        int sum = n;

        for(int i = 0; i < n; i++) {
            sum += i;
        }
        return sum;
    }
}

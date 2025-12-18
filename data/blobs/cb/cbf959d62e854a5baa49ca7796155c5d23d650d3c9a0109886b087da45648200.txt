package com.leetcode.m649_predict_party_victory;

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Integer> radiantQueue = new LinkedList<>();
        Queue<Integer> direQueue = new LinkedList<>();

        for (int i = 0; i < senate.length(); i ++) {
            if (senate.charAt(i) == 'R') {
                radiantQueue.add(i);
            } else {
                direQueue.add(i);
            }
        }

        int n = senate.length();
        while (!radiantQueue.isEmpty() && !direQueue.isEmpty()) {
            int rIdx = radiantQueue.remove();
            int dIdx = direQueue.remove();
            if (rIdx < dIdx) {
                radiantQueue.add(rIdx + n);
            } else {
                direQueue.add(dIdx + n);
            }
        }

        return radiantQueue.isEmpty()? "Dire": "Radiant";
    }
}
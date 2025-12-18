package src.Medium;
// Time Comlexity: O(n)

import java.util.*;
class Solution {
    public int minimumRounds(int[] tasks) {
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        for (int i : tasks) count.put(i, count.getOrDefault(i, 0) + 1);
        int total = 0;
        for (int i : count.values()) {
            if (i == 1) return -1;
            if (i % 3 == 1) {
                if (i == 4) total += 2;
                else total += (i - 4) / 3 + 2;
            } else if (i % 3 == 0) {
                total += i / 3;
            } else {
                total += (i - 2) / 3 + 1;
            }
        }
        return total;
    }
}
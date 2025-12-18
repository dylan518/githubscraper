import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] dice = {a, b, c, d};
        Arrays.sort(dice);
        Map<Integer, Integer> countMap = new HashMap<>();

        for (int num : dice) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        List<Integer> counts = new ArrayList<>(countMap.values());
        Collections.sort(counts, Collections.reverseOrder());

        int distinctNums = countMap.size();

        if (distinctNums == 1) {
            return 1111 * dice[0];
        } else if (distinctNums == 2) {
            if (counts.get(0) == 3) {
                int p = -1, q = -1;
                for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
                    if (entry.getValue() == 3) p = entry.getKey();
                    if (entry.getValue() == 1) q = entry.getKey();
                }
                return (10 * p + q) * (10 * p + q);
            } else if (counts.get(0) == 2) {
                int[] nums = new int[2];
                int index = 0;
                for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
                    if (entry.getValue() == 2) {
                        nums[index++] = entry.getKey();
                    }
                }
                return (nums[0] + nums[1]) * Math.abs(nums[0] - nums[1]);
            }
        } else if (distinctNums == 3) {
            int p = -1, q = -1, r = -1;
            for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
                if (entry.getValue() == 2) p = entry.getKey();
                if (entry.getValue() == 1) {
                    if (q == -1) q = entry.getKey();
                    else r = entry.getKey();
                }
            }
            if (p != -1 && q != -1 && r != -1) {
                return q * r;
            }
        } else if (distinctNums == 4) {
            return dice[0];
        }

        return 0;
    }
}
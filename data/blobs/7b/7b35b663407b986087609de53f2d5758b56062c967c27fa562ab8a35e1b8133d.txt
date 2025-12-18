package algorithms.arrays;

import java.util.HashMap;
import java.util.Map;

class CountNicePairs {

    public static int countNicePairs(int[] nums) {
        int res = 0, mod = (int)1e9 + 7;
        Map<Integer, Integer> count = new HashMap<>();;
        for (int a : nums) {
            int b = rev(a), v = count.getOrDefault(a - b, 0);
            count.put(a - b, v + 1);
            res = (res + v) % mod;
        }
        return res;
    }

    private static int rev(int x) {
        return Integer.parseInt(new StringBuilder().append(x).reverse().toString());
    }

    public static void main(String[] args) {
        int[] heights = {13,10,35,24,76};
        System.out.println(countNicePairs(heights));
    }

}
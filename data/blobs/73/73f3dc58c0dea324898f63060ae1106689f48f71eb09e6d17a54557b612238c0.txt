package src.com.daily.dsa.challenge.leetcode;

import java.util.ArrayList;
import java.util.List;

public class CombinationSum {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();

        combinations(nums, res, new ArrayList<Integer>(), target, 0);
        return res;
    }


    private void combinations(int[] nums, List<List<Integer>> res, List<Integer> current, int target, int index) {
        if (target == 0) {
            res.add(new ArrayList<>(current));
            return;
        } else if (target < 0) {
            return;
        }

        for (int x = index; x < nums.length; x++) {
            current.add(nums[x]);
            combinations(nums, res, current, target - nums[x], x);
            current.remove(current.size() - 1);
        }
    }



}

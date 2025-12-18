package main.prep2021.casestudies.combinations;

import java.util.LinkedList;
import java.util.List;

public class CombinationsV3 {
    private final List<List<Integer>> answer = new LinkedList<>();
    int n;
    int k;

    private void recur(int number, LinkedList<Integer> combination) {
        if (combination.size() == k) {
            answer.add(new LinkedList<>(combination));
            return;
        }

        for (int i = number; i <= n; i++) {
            combination.add(i);
            recur(i + 1, combination);
            combination.removeLast();
        }
    }

    public List<List<Integer>> combine(int n, int k) {
        this.n = n;
        this.k = k;
        recur(1, new LinkedList<>());
        return answer;
    }

    public static void main(String[] args) {
        CombinationsV3 solution = new CombinationsV3();
        List<List<Integer>> answer = solution.combine(4, 3);
        for (List<Integer> combination : answer) {
            System.out.println(combination.toString());
        }
//        List<List<Integer>> answer = solution.combine(1, 1);
//        for (List<Integer> combination : answer) {
//            System.out.println(combination.toString());
//        }
    }
}

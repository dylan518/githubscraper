package co.axelrod.leetcode;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * https://leetcode.com/problems/pascals-triangle/
 */
class PascalTriangle {
    @Test
    void generateTest() {
        assertEquals(
                List.of(
                        List.of(1),
                        List.of(1, 1),
                        List.of(1, 2, 1),
                        List.of(1, 3, 3, 1),
                        List.of(1, 4, 6, 4, 1)
                ),
                generate(5)
        );
    }

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(List.of(1));

        for (int i = 1; i < numRows; i++) {
            List<Integer> prev = result.get(i - 1);
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for (int j = 0; j < i - 1; j++) {
                int left = prev.get(j);
                int right = prev.get(j + 1);
                row.add(left + right);
            }
            row.add(1);

            result.add(row);
        }

        return result;
    }
}

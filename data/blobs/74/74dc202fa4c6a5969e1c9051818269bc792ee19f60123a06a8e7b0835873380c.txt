package org.example.Hashmap;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LongestConsecutiveSequenceTest {
    @Test
    public void testLongestConsecutive() {
        LongestConsecutiveSequence sequence = new LongestConsecutiveSequence();

        // Test Case 1: Empty input
        int[] emptyArray = {};
        assertEquals(0, sequence.longestConsecutive(emptyArray));

        // Test Case 2: Consecutive sequence
        int[] consecutiveArray = {1, 2, 3, 4, 5};
        assertEquals(5, sequence.longestConsecutive(consecutiveArray));

        // Test Case 3: Random sequence
        int[] randomArray = {100, 4, 200, 1, 3, 2};
        assertEquals(4, sequence.longestConsecutive(randomArray));

        // Test Case 4: Duplicate elements
        int[] duplicateArray = {1, 2, 2, 3, 4, 4, 5};
        assertEquals(5, sequence.longestConsecutive(duplicateArray));

        // Test Case 5: Negative and zero values
        int[] negativeArray = {-1, 0, -2, -3};
        assertEquals(4, sequence.longestConsecutive(negativeArray));
    }

}
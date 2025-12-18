package org.arif.DAILY_CHALANGE;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MakeGoodTest {

    @Test
    void makeGood() {
        MakeGood good = new MakeGood();
        String actual = "leEeetcode";
        String expected = "leetcode";
        assertEquals(expected,good.makeGood(actual));
    }
}
package com.example.productservicesst;

import org.junit.jupiter.api.Test;

import java.beans.Transient;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class RandomTest {

    @Test
    void testIsOnePlusOneIsTwo(){
        int i = 1+1;

        assert i == 2;

        assertEquals(4, i, "i is not equal to 4 so the testcase is failing");
    }
}

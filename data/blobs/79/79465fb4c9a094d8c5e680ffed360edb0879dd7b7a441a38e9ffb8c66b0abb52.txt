package com.algorithms.datastructures.backtracking;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class BacktrackingTest {
    private Backtracking sut;

    @BeforeEach
    public void setUp() {
        sut = new Backtracking();
    }

    @Test
    public void generateParenthesis() {
        List<String> parenthesis = sut.generateParenthesis(3);
        assertEquals("((()))", parenthesis.get(0));
    }
}

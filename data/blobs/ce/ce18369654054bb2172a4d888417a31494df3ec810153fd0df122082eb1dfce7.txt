/* (C)2023 */
package io.github.andrewfitzy.day_12;

import static org.junit.jupiter.api.Assertions.assertEquals;

import io.github.andrewfitzy.TaskInputReader;
import java.util.Arrays;
import java.util.List;
import org.junit.jupiter.api.Test;

public class TestTask01 {
    @Test
    void demoTestMethod_01() {
        Task01 task01 = new Task01(Arrays.asList("[1,2,3]"));

        int result = task01.solve();

        assertEquals(6, result);
    }

    @Test
    void demoTestMethod_02() {
        Task01 task01 = new Task01(Arrays.asList("{\"a\":2,\"b\":4}"));

        int result = task01.solve();

        assertEquals(6, result);
    }

    @Test
    void demoTestMethod_03() {
        Task01 task01 = new Task01(Arrays.asList("[[[3]]]"));

        int result = task01.solve();

        assertEquals(3, result);
    }

    @Test
    void demoTestMethod_04() {
        Task01 task01 = new Task01(Arrays.asList("{\"a\":{\"b\":4},\"c\":-1}"));

        int result = task01.solve();

        assertEquals(3, result);
    }

    @Test
    void demoTestMethod_05() {
        Task01 task01 = new Task01(Arrays.asList("[]"));

        int result = task01.solve();

        assertEquals(0, result);
    }

    @Test
    void demoTestMethod_06() {
        Task01 task01 = new Task01(Arrays.asList("{}"));

        int result = task01.solve();

        assertEquals(0, result);
    }

    // @Test
    void testSolveWithRealData() {
        List<String> fileContent = TaskInputReader.getFileContent("./day_12/task01_input.txt");

        Task01 task01 = new Task01(fileContent);
        int result = task01.solve();

        assertEquals(191164, result);
    }
}

package edu.wctc.calculator;

import org.junit.jupiter.api.Test;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

import static org.junit.jupiter.api.Assertions.*;

public class OtherTests {
    @Test
    void testArrayAssertion() {
        String[] a = {"Hello", "world"};
        String[] b = {"Hello", "world"};
        assertArrayEquals(a, b, "Arrays do not contain the same things");
    }

    @Test
    void testEqualAssertion() {
        LocalDate a = LocalDate.of(2002, 9, 29);
        LocalDate b = LocalDate.of(2002, 9, 29);
        assertEquals(a, b, "Dates do not represent the same date");
    }

    @Test
    void testNotNull() {
        LocalDateTime now = LocalDateTime.now();
        assertNotNull(now, "Now should not be null!");
    }

    @Test
    void testSameAssertion() {
        LocalDate a = LocalDate.of(2002, 9, 29);
        LocalDate b = LocalDate.of(2002, 9, 29);
        assertSame(a, b, "Dates are not the same object");
    }

    @Test
    void testTrue() {
        LocalTime a = LocalTime.now();
        LocalTime b = LocalTime.now();
        assertTrue(a.compareTo(b) < 0, "First time is not before the second time");
    }


}

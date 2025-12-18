package org.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class StringProcessorTest {

    private StringProcessor processor;

    @BeforeEach
    void setUp() {
        processor = new StringProcessor();
    }

    @Test
    void testCopies() {
        assertEquals("Hello\nHello\nHello", processor.Copies(3, "Hello"));
        assertEquals(" ", processor.Copies(0, "Hello"));
        assertEquals("Ошибка!!", processor.Copies(-1, "Hello"));
    }

    @Test
    void testEntries() {
        assertEquals(2, processor.Entries("hello world, hello Java", "hello"));
        assertEquals(0, processor.Entries("hello world, hello Java", "Python"));
        assertEquals(-1, processor.Entries("hello world", ""));
        assertEquals(-2, processor.Entries("", "hello world"));
    }

    @Test
    void testReplace() {
        assertEquals("одиндватри", processor.Replace("123"));
        assertEquals("один два три", processor.Replace("1 2 3"));
        assertEquals("test", processor.Replace("test"));
    }

    @Test
    void testDelete() {
        StringBuilder input = new StringBuilder("123456");
        processor.Delete(input);
        assertEquals("135", input.toString());

        input = new StringBuilder("a b c d e f");
        processor.Delete(input);
        assertEquals("ace", input.toString());
    }
}

package com.kodilla.stream.array;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ArrayOperationsTestSuite {
    @Test
    void testGetAverage(){
        //Given
        int[] numbersList = {1, 2, 3, 4, 5, 6 ,7 ,8 ,9 };
        //When
        double average = ArrayOperations.getAverage(numbersList);
        //Then
        assertEquals(4, average);
    }
}

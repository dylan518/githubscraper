import org.example.Numbers;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class NumberTest {

    private Numbers numbers;


    @ParameterizedTest
    @ValueSource(ints = {3, 23, 311, 487, 653, 947})
    void testIsPrime(int number) {
        numbers = new Numbers();
        assertTrue(numbers.isPrime(number));


    }

    @ParameterizedTest
    @ValueSource(ints = { 23, 46, 115, 184, 207,230})
    void testIsMultiple(int number) {
        numbers = new Numbers();
        assertTrue(numbers.isMultiple(number, 23));

    }

    @ParameterizedTest
    @ValueSource(ints = {32, 64, 2, 20, 30, 26})
    void testIsEven(int number) {
        numbers = new Numbers();
        assertTrue(numbers.isEven(number));
    }


}

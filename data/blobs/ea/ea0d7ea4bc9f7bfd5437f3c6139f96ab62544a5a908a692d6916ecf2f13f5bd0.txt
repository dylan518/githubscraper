package consultation2023_12_21;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class TestConsultation2023_12_21 {

    @Test
    public void testDoubleReturnType() {
        double expected = 1.123;
        double result = Consultation2023_12_21.methodForDoubleTesting();

        // 0.001 (дельта) - преемлемое отклоненение result от expected,
        // в случае, если разница между expected и result меньше,
        // чем дельта, то тест будет считаться успешно пройденным.
        // ВАЖНО! дельта определяется автором теста!
        Assertions.assertEquals(expected, result, 0.001);
    }
}

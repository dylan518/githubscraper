package leetcode;

import static org.assertj.core.api.Assertions.*;

import org.junit.jupiter.api.Test;

class L1404NumberOfStepsToReduceANumberInBinaryRepresentationToOneTest {

    @Test
    void numSteps() {
        // given
        L1404NumberOfStepsToReduceANumberInBinaryRepresentationToOne solution = new L1404NumberOfStepsToReduceANumberInBinaryRepresentationToOne();
        String s = "10";

        // when
        int answer = solution.numSteps(s);

        // then
        assertThat(answer).isEqualTo(1);
    }

}

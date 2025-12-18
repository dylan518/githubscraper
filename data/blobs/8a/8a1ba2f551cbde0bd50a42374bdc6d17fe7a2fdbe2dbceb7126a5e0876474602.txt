package leetcode_categories.arrays_hashings;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class L169MajorityElementTest {
    L169MajorityElement myClass;

    @BeforeEach
    void setUp() {
        myClass = new L169MajorityElement();
    }

    @Test
    public void testFirst() {
        //Given
        int[] nums = new int[] {3,2,3};
        //When
        int actual = myClass.majorityElement(nums);
        //Then
        assertEquals(3, actual);
    }

    @Test
    public void testSecond() {
        //Given
        int[] nums = new int[] {2,2,1,1,1,2,2};
        //When
        int actual = myClass.majorityElement(nums);
        //Then
        assertEquals(2, actual);
    }

}
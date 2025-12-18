import org.junit.jupiter.api.Test;

import static com.google.common.truth.Truth.assertThat;
public class TestSort_JUnit{
    /** Tests the sort method of the Sort class. */
    @Test//函数必须为非静态，将把错误修复和设计游戏化
    public void testSort() {
        String[] input = {"cows", "dwell", "above", "clouds"};
        String[] expected = {"above", "clouds", "cows", "dwell"};
        Sort.sort(input);

        assertThat(input).isEqualTo(expected);
    }
    @Test
    public void testFindSmallest() {
        String[] input = {"rawr", "a", "zaza", "newway"};
        int expected = 1;
        int actual = Sort.findSmallest(input,0);
        assertThat(actual).isEqualTo(expected);

        String[] input2 = {"there", "are", "many", "pigs"};
        int expected2 = 2;

        int actual2 = Sort.findSmallest(input2,2);
        assertThat(actual2).isEqualTo(expected2);
    }

    public static void testSwap() {
        String[] input = {"i", "have", "an", "egg"};
        int a = 0;
        int b = 2;
        String[] expected = {"an", "have", "i", "egg"};

        Sort.swap(input, a, b);
        assertThat(expected).isEqualTo(input);
    }

    public static void main(String[] args) {
        //testFindSmallest();
        //testSwap();
        //testSort();
    }
}
package tips.util;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class ArraysTest {

    /**
     * Arrays 는 배열에 적용할 수 있는 여러 메서드를 제공하는 클래스 (생성자가 private 이라 객체로 생성하여 사용하지 않는다.)
     * - 정렬, 비교, stream 반환, List 반환 등 많은 메서드를 제공한다.
     *
     */
    public static void main (String[] args) {
        Integer[] a = new Integer[3];
        a[0] = 3;
        a[1] = 2;
        a[2] = 1;

        Arrays.sort(a);
        List<Integer> b =  Arrays.asList(a);
        System.out.println(b);
        Stream c  = Arrays.stream(a);

        Integer[] d = {3, 2, 1};
        Arrays.compare(a, d); // 배열요소의 타입이 Comparable을 구현하여야 한다.
        System.out.println(Arrays.compare(a, d));
    }

}

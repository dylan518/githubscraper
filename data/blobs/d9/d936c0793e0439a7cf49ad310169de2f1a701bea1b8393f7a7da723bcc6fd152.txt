package lesson;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.concurrent.ThreadLocalRandom;

public class CountingSort {
    public static void main(String[] args) {
        Integer[] arr = new Integer[20];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = ThreadLocalRandom.current().nextInt(1, 5);
        }

        Arrays.stream(arr).forEach(i -> System.out.print(i + ", "));
        sort(arr);

        System.out.println();

        Arrays.stream(arr).forEach(i -> System.out.print(i + ", "));
    }

    private static <T extends Comparable<T>> void sort(T[] arr) {
        Map<T, Integer> elements = new TreeMap<>();
        for (T key : arr) {
            if (elements.containsKey(key)) {
                elements.put(key, elements.get(key) + 1);
            } else {
                elements.put(key, 1);
            }
        }

        int counter = 0, val;
        T tmp;

        for (Map.Entry<T, Integer> el : elements.entrySet()) {
            val = el.getValue();
            tmp = el.getKey();
            for (int i = 0; i < val; i++) {
                arr[counter++] = tmp;
            }
        }
    }


}

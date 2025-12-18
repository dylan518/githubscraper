package edu.fabzdev.generics;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

/**
 *
 * @author fabio
 */
public class SortDemo {

    public static void sortDemo1() {
        String[] arr = {"x", "m", "c", "w", "a", "f", "d"};

        for (String s : arr) {
            System.out.print(s + ", ");
        }
        System.out.println();

        Arrays.sort(arr);
        for (String s : arr) {
            System.out.print(s + ", ");
        }
        System.out.println();

        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                /*
                > 0  : Mayor
                < 0  : Menos
                == 0 : igual
                 */
                int comparador = o1.compareTo(o2);
                if (comparador > 0) {
                    return -1;
                } else if (comparador < 0) {
                    return 1;
                }
                return 0;
            }

        });
        for (String s : arr) {
            System.out.print(s + ", ");
        }
        System.out.println();
    }

    public static void sortDemo2() {
        List<String> arr2 = new ArrayList<>();
        arr2.add("x");
        arr2.add("m");
        arr2.add("c");
        arr2.add("w");
        arr2.add("a");
        arr2.add("f");
        arr2.add("d");
        arr2.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.compareTo(o2) > 0) {
                    return -1;
                } else if (o1.compareTo(o2) < 0) {
                    return 1;
                }
                return 0;
            }

        });
        for (String s : arr2) {
            System.out.print(s + ", ");
        }
        System.out.println();

    }

    public static void main(String[] args) {
//        sortDemo1();
        sortDemo2();
    }
}

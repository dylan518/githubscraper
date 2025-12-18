package org.exercise.lexicagraphicalOrder.streams;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Streams {
    /*
    * 8. Write a Java program to find the second smallest and largest elements in a list of integers using streams.
    * */
    public static void main(String[] args) {
//        List<Integer> integers = Arrays.asList(4, 7, 9, 2, 3, 10);
//        findSecondSmallestAndLargest(integers);
//
//        String[] arr = new String[]{"a", "b", "c"};
//        Stream<String> streamOfArrayFull = Arrays.stream(arr);
//        Stream<String> streamOfArrayPart = Arrays.stream(arr, 1, 3);
//
//        Stream<Integer> streamIterated = Stream.iterate(40, n -> n + 2).limit(10);
//        streamIterated.forEach(n -> System.out.println(n));

        Stream<Integer> from1to100 = Stream.iterate(1, n -> n + 1).limit(100);
        //from1to100.forEach(n -> System.out.println(n));
        from1to100.forEach(n -> {

            if (n % 15 == 0) {
                System.out.println(n);
                System.out.println("FizzBuzz");
            } else if (n % 5 == 0) {
                System.out.println(n);
                System.out.println("Buzz");
            } else if (n % 3 == 0) {
                System.out.println(n);
                System.out.println("Fizz");
            }
        });
    }

    private static void findSecondSmallestAndLargest(List<Integer> numbers){
        if(numbers.size() < 2){
            System.out.println("The list must have more than 2 numbers");
            return;
        }
        int secondSmallest = numbers.stream()
                .distinct()
                .sorted()
                .skip(1)
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Unable to find second smallest element."));

        int secondLargest = numbers.stream()
                .distinct()
                .sorted((a, b) -> Integer.compare(b, a))
                .skip(1)
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Unable to find second largest element."));

        System.out.println("Second Smallest Element: " + secondSmallest);
        System.out.println("Second Largest Element: " + secondLargest);
    }
}

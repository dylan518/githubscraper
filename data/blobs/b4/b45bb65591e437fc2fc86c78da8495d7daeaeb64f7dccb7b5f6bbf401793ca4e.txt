package org.solutions;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Day14_Scope {

    /**
     * Problem Statement -
     * [Scope](https://www.hackerrank.com/challenges/30-scope)
     */
    public static void main(String[] args) {
        Scanner e = new Scanner(System.in);
        int n = Integer.parseInt(e.nextLine());
        List<Integer> arr = new ArrayList<>();

        IntStream.range(0, n).forEach(i -> {
            arr.add(e.nextInt());
        });
        e.close();
        Scope scope = new Scope(arr);
        scope.computeDifference();
        System.out.println(scope.getMaximumDifference());
    }
}

class Scope {
    private int maximumDifference;
    private List<Integer> elements;

    Scope(List<Integer> elements) {
        this.elements = elements;
    }

    void computeDifference() {
        int difference;
        for (int i = 0; i < elements.size(); i++) {
            for (int j = i + 1; j < elements.size(); j++) {
                difference = Math.abs(elements.get(i) - elements.get(j));
                if (difference > maximumDifference)
                    maximumDifference = difference;
            }
        }
    }

    public int getMaximumDifference() {
        return maximumDifference;
    }
}
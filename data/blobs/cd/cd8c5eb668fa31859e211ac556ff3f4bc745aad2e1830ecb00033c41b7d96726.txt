package org.example;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;


public class Main {
    static BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {

        List<Integer> nm = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt)
            .collect(Collectors.toList());

        List<Integer> first = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt)
            .collect(Collectors.toList());

        List<Integer> second = Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt)
            .collect(Collectors.toList());

        ArrayList<Integer> list = new ArrayList<>(first);
        list.addAll(second);

        quickSort(list, 0, list.size() - 1);

        for (Integer item : list) {
            wr.write(item + " ");
        }

        wr.flush();
        wr.close();
        br.close();
    }

    private static void quickSort(ArrayList<Integer> list, int left, int right) {
        if (left >= right) {
            return;
        }

        int pivot = sort(list, left, right);

        quickSort(list, left, pivot - 1);
        quickSort(list, pivot + 1, right);
    }

    private static int sort(ArrayList<Integer> list, int left, int right) {
        int pivot = list.get(left);
        int i = left;
        int j = right;

        while (i < j) {
            while (pivot < list.get(j) && i < j) {
                j--;
            }

            while (pivot >= list.get(i) && i < j) {
                i++;
            }

            swap(list, i, j);
        }
        swap(list, left, i);

        return i;
    }

    private static void swap(ArrayList<Integer> list, int i, int j) {
        int data = list.get(i);
        list.set(i, list.get(j));
        list.set(j, data);
    }


}


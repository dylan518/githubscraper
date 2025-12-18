package sorting_searching;

import java.util.Scanner;


public class BubbleSort {

    public int[] solution(int n, int[] arr) {
        for (int i = 0; i < n-1; ++i) {
            for (int j = 0; j < n - i - 1; ++j) {
                int tmp = arr[j];
                if (arr[j] > arr[j + 1]) {
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                }

            }
        }

        return arr;
    }

    public static void main(String[] args) {
        BubbleSort main = new BubbleSort();
        Scanner scan = new Scanner((System.in));

        int n = scan.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; ++i) {
            arr[i] = scan.nextInt();
        }
        int[] result = main.solution(n, arr);
        for (int x : result) {
            System.out.print(x + " ");
        }

    }
}

import java.util.Arrays;

public class ArrayDuplicates {
    public static void main(String[] args) {
        int[] arr = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7 };
        findDuplicates(arr);
    }

    static void findDuplicates(int[] arr) {
        if (arr.length == 0) {
            System.out.println("Array is empty");
            return;
        }
        int start = 0;
        int end = 1;
        int[] duplicates = new int[arr.length];
        int index = 0;
        while (end < arr.length) {
            if (arr[start] == arr[end]) {
                if (!checkItContains(duplicates, arr[start])) {
                    duplicates[index++] = arr[start];
                }
                System.err.println("Current filled element:" + duplicates[index - 1]);
                start++;
                System.err.println("CURRENT START:" + start);
                end = start;
            }
            end++;
            if (end + 1 == arr.length) {
                start++;
                end = start + 1;
            }

        }
        if (index == 0) {
            System.out.println("[]");
            return;
        }

        System.err.println(Arrays.toString(duplicates));
    }

    static boolean checkItContains(int[] duplicates, int value) {
        for (int i = 0; i < duplicates.length; i++) {
            if (value == duplicates[i])
                return true;
        }
        return false;
    }
}

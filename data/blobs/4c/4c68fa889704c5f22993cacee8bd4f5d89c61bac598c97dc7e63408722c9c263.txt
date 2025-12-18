import java.util.Arrays;

public class MainProgram {

    public static void main(String[] args) {
        // write your test code here
        int[] array = { 8, 3, 7, 9, 1, 2, 4, 2, 6, 7, 9, 23, 1, 2, 6, 8, 1, 23, 8, 2, 8, 1, 799, 168, 68 };

        System.out.println("start:    " + Arrays.toString(array));
        MainProgram.sort(array);
        System.out.println("sorted:   " + Arrays.toString(array));
    }

    public static int smallest(int[] array) {
        int smallest = array[0];
        // System.out.println(smallest);
        // System.out.println(array.length);
        for (int i = 0; i < array.length; i++) {
            // System.out.println("for loop: " + array[i]);
            if (array[i] < smallest) {
                smallest = array[i];
                // System.out.println("smallest: " + smallest);
            }
        }
        // System.out.println(smallest);
        return smallest;
    }

    public static int indexOfSmallest(int[] array) {
        int smallest = array[0];
        int indexOfSmallest = 0;

        for (int i = 0; i < array.length; i++) {
            // System.out.println("for loop: " + array[i]);
            if (array[i] < smallest) {
                smallest = array[i];
                indexOfSmallest = i;
            }
        }
        return indexOfSmallest;
    }

    public static int indexOfSmallestFrom(int[] table, int startIndex) {
        int smallest = table[startIndex];
        // System.out.println("smallest in 3: " + smallest);
        int indexOfSmallest = startIndex;
        // System.out.println("smallest in 3: " + indexOfSmallest);

        for (int i = indexOfSmallest; i < table.length; i++) {
            // System.out.println("for loop: " + table[i]);
            if (table[i] < smallest) {
                smallest = table[i];
                indexOfSmallest = i;
            }
        }
        return indexOfSmallest;
    }

    public static void swap(int[] array, int index1, int index2) {
        int arrayTempIndex = array[index1];
        array[index1] = array[index2];
        array[index2] = arrayTempIndex;
    }

    public static void sort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.println("sorting:  " + Arrays.toString(array));
            swap(array, indexOfSmallestFrom(array, i), i);
            indexOfSmallestFrom(array, i);
        }
    }

}

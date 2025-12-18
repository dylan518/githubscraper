package DynamicArray;

import java.util.*;

public class DynamicArray<T> {

    int[] arg;
    int lastIndex = 0;

    // lastIndex will act as the size variable as well as the last empty space
    public DynamicArray() {
        arg = new int[20];
    }

    public DynamicArray(final int capacity) {
        arg = new int[capacity];
    }

    // Checks is the lastIndex is outside the array
    // copies and doubles the array
    // Adds element and increments lastIndex
    public void add(final int element) {
        if (lastIndex >= arg.length) {
            arg = Arrays.copyOf(arg, arg.length * 2);
        }
        arg[lastIndex] = element;
        lastIndex++;
    }

    // Tries to hold the element, if index is out of bounds,
    // just returns 0 and that's it
    // then slides each element after to the index below
    // reduces lastIndex, if lastIndex is half the array length,
    // copies the array to a halved array, returns the removed element
    public int remove(final int idx) {
        int removedItem;
        try {
            removedItem = arg[idx];
        } catch (Exception e) {
            return 0;
        }
        for (int i = idx; i < lastIndex - 1; i++) {
            arg[i] = arg[i + 1];
        }
        lastIndex--;
        if (arg.length > 20 && lastIndex <= arg.length / 2) {
            arg = Arrays.copyOf(arg, arg.length / 2);
        }
        return removedItem;
    }

    public void put(final int idx, int element) {
        arg[idx] = element;
    }

    public int get(final int idx) {
        return arg[idx];
    }

    // lastIndex follows the size with each add() and remove()
    public int get_size() {
        return lastIndex;
    }

    public int get_capacity() {
        return arg.length;
    }

    // If size returns 0, the array is empty
    public boolean is_empty() {
        if (this.get_size() == 0) {
            return true;
        } else {
            return false;
        }
    }

}
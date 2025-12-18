package Example;


import java.util.*;

public class GenericPair{
    public static void main(String[] args) {
        Pair<String, Integer> pair = new Pair<>("One", 1);
        System.out.println(pair.getFirst() + ", " + pair.getSecond()); // Output: ?

        ArrayDeque<Pair> pairs1 = new ArrayDeque<>();
        HashSet<Pair> pairs2 = new HashSet<>();
        TreeSet<Pair> pairs3 = new TreeSet<>();
        Stack<Pair> pairs4 = new Stack<>();

        ArrayList<Integer> list = new ArrayList<Integer>();

        list.sort();
    }


    public static <T extends Comparable<T>> T findMax(T[] array) {
        if (array == null || array.length == 0)
            return null;

        Arrays.sort(array);
        return array[array.length - 1];
    }
}
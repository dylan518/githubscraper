package NewØvelse;

import java.util.ArrayList;
import java.util.List;

public class Partition {
    public static void partition(List<Integer> lst, int E) {
        List<Integer> lessThanE = new ArrayList<>();
        List<Integer> greaterThanE = new ArrayList<>();

        for (int x : lst) {
            if (x <= E) {
                lessThanE.add(x);
            } else {
                greaterThanE.add(x);
            }
        }

        lst.clear();
        lst.addAll(lessThanE);
        lst.addAll(greaterThanE);
    }

    public static void main(String[] args) {
        List<Integer> lst = new ArrayList<>();
        lst.add(15);
        lst.add(1);
        lst.add(6);
        lst.add(12);
        lst.add(-3);
        lst.add(4);
        lst.add(8);
        lst.add(21);
        lst.add(2);
        lst.add(30);
        lst.add(-1);
        lst.add(9);

        partition(lst, 4);
        System.out.println(lst); // Output: [-3, 1, 4, 2, -1, 15, 6, 12, 8, 21, 30, 9]
    }
}



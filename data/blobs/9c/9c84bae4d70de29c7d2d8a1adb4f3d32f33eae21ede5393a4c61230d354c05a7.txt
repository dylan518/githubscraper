package advanced.deque;

import java.util.Deque;
import java.util.Iterator;
import java.util.LinkedList;

public class Imp {
    public static void main(String[] args) {
        Deque<Integer> deq = new LinkedList<>();
        int X = 2;

        deq.add(1);
        deq.add(2);
        deq.add(3);
        deq.add(4);
        deq.add(5);
        deq.add(6);

        Iterator<Integer> it = deq.iterator();

        while (it.hasNext()){
            it.remove();

        }


        System.out.println(deq);
    }
}

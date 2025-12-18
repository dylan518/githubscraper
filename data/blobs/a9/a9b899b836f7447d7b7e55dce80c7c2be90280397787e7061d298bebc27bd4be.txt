import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        System.out.println(countResult());

printOutList();
    }

    private static int countResult() {
        int a = 1;
        try {
            a = a + 1;
            a = a / 0;
            return a;
        } catch (Exception e) {
            a = a + 3;
        } finally {
            a++;
        }
        return a;
    }

    private static void printOutList() {
        List<Integer> list = new ArrayList<>();

        list.add(20);
        list.add(80);
        list.add(10);
        list.add(180);
        Collections.sort(list);
        list.remove(2);
        for (Integer listElement : list)
            System.out.print(listElement + "");


    }

}



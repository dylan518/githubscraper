import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int[] array = new int[10];
        array[0] = 1;
        System.out.println(Arrays.toString(array));


        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(3);
        list.remove(0);//удалить индекс
        int result = list.get(0);
//        list.clear();
//        list.set(0, 56);//заменить ячейку
        boolean res = list.contains(56);
        System.out.println(list);
        System.out.println(res);
        System.out.println(result);
    }
}

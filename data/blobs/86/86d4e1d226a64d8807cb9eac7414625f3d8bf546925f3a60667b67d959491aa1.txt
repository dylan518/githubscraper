package warmUpQuestions;

import com.google.common.collect.ObjectArrays;
import com.google.common.primitives.Ints;

import java.util.*;

public class JoinTwoArraysusingGuava_List_Hashset {

    public static void main(String[] args) {
        Integer[] firstgroup = {1, 2, 3, 4, 5};
        Integer[] secondGroup = {4, 5, 6, 7, 8};

        List<Integer> list1 = new ArrayList<>(List.of(firstgroup));
        List<Integer> list2 = new ArrayList<>(List.of(secondGroup));
        list1.addAll(list2);
        System.out.println(list1);
        //////////////

        HashSet<Integer> set = new HashSet<>(Set.of(firstgroup));
        HashSet<Integer> set2 = new HashSet<>(Set.of(secondGroup));
        set.addAll(set2);
        System.out.println(set);

        //below we use google guava
        Integer[] arr = ObjectArrays.concat(firstgroup, secondGroup, Integer.class);
        List<Integer> list = Arrays.asList(arr);
        System.out.println(list);
        // for primitive type arrays
        int[] firstgroup1 = {1, 2, 3, 4, 5};
        int[] secondGroup2 = {4, 5, 6, 7, 8};
        int[] son = Ints.concat(firstgroup1, secondGroup2);
        //we can convert primitve int to list of integer by guava
        List<Integer> output = Ints.asList(son);
        System.out.println(output);
        //we can convert int to list of integer by help of iteration
        List<Integer> output2 = new ArrayList<Integer>();
        for (int value : son) {
            output2.add(value);
        }
        System.out.println(output2);
    }

}

package arraysandhashing;

import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for(int num: nums) {
            if(set.contains(num)){
                return true;
            }
            set.add(num);
        }
        return false;
    }

    public static boolean containsDuplicate2(int[] nums){
        Set<Integer> set = new HashSet<>();

        for(int num: nums){
            if(set.contains(num)) return true;
            set.add(num);
        }
        return false;
    }
}

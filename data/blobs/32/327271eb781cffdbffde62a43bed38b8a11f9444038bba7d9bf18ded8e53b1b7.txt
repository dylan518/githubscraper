package collections;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Pangram {
    public static boolean checkString(String s) {
        Set<String> set = new HashSet<>(Arrays.asList(s.replaceAll("\\s", "").split("")));
        return set.size() == 26;
    }

    public static void main(String[] args) {
        String str = "Jackdaws love my big sphinx of quartz";
        System.out.println(checkString(str));
    }
}
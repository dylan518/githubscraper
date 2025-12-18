package BASIC;
import java.util.*;
public class J11_map {
    public static void main(String[] args) {
//        Map<Integer,Integer> mp=new HashMap<Integer,Integer>();
        Map<Integer, Integer> mp = new LinkedHashMap<Integer, Integer>(); // it stores element as it is
//        Map<Integer,Integer> mp=new TreeMap<Integer,Integer>();  // store element in ascending order
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            mp.put(sc.nextInt(), sc.nextInt());
        }
        for (Map.Entry<Integer, Integer> it : mp.entrySet()) {
            System.out.println(it.getKey() + " = " + it.getValue());
        }

        System.out.println(mp.size());  //return size

        System.out.println(mp.containsKey(2));
        System.out.println(mp.containsValue(20));
    }
}
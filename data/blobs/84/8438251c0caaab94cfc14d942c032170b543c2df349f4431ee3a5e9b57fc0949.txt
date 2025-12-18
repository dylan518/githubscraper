package CoreJava.collections;

import java.util.HashMap;
import java.util.Map;

public class Output2 {
  public static void main(String[] args) {
    Output2 p = new Output2();
    p.start();
    getDeets();

    /**
     * Object[] objects = {new Integer(12), new String("foo"), new Integer(5), new Boolean(true)};
     * Arrays.sort(objects); for (int i = 0; i < objects.length; i++) {
     * System.out.print(objects[i].toString()); System.out.print(" "); }
     */
  }

  public static void getDeets() {
    Map<String, Integer> map = new HashMap<>();
    String a = "abc";
    String b = new String("abc");
    map.put(a, 10);
    map.put(b, 20);
    map.put(new String("abc"), 30);
    System.out.println(map.get("abc"));
  }

  void start() {
    long[] a1 = {3, 4, 5};
    long[] a2 = fix(a1);
    System.out.println(a1[0] + a1[1] + a1[2] + " ");
    System.out.println(a2[0] + a2[1] + a2[2]);
  }

  private long[] fix(long[] a1) {
    a1[1] = 7;
    return a1;
  }
}

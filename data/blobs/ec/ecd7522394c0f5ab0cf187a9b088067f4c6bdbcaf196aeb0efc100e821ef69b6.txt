import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListExample {
  public static void main(String[] args) {
    // Syntax
    Scanner in = new Scanner(System.in);

    ArrayList<Integer> list = new ArrayList<>(10);

    for (int i = 0; i < 5; i++) {
      list.add(in.nextInt());
    }

    for (int j = 0; j < 5; j++) {
      System.out.println(list.get(j));
    }
  }
}

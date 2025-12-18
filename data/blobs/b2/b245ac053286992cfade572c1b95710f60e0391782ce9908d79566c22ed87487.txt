package lesson23_generics_PECS.task3;

public class Main {
   public static void main(String[] args) {

      Box<String> stringBox = new Box<>();
      Box<Integer> integerBox = new Box<>();

      stringBox.putItem("Hello!");
      integerBox.putItem(7);

      System.out.println(stringBox.getItem().length());
      System.out.println(integerBox.getItem() + 5);
   }
}

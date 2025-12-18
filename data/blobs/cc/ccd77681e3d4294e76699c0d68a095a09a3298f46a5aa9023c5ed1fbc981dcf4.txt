import java.util.ArrayList;

public class Box<T extends Fruit> {

    private ArrayList<T> fruits;

    public Box() {
        this.fruits = new ArrayList<>();
    }

    private float getBoxWeight() {
        float weight = 0;
        for (T t : fruits) {
            weight += t.getWeight();
        }
        return weight;
    }

    public void addFruit(T fruit) {
        fruits.add(fruit);
    }

    public boolean compare(Box box) {
        return box.getBoxWeight() == this.getBoxWeight() ? true : false;
    }

    public void moveFruitsToOtherBox(Box<T> box) {
        for (T t : fruits) {
            box.addFruit(t);
        }
        fruits.clear();
    }

    @Override
    public String toString() {
        String whatInsideList = new String();
        if (fruits.size() == 0) {
            whatInsideList = "пустота";
        } else {
            whatInsideList = (fruits.get(0).getClass().getName() == "Apple") ? "яблоки" : "апельсины";
        }
        return String.format("Вес коробки %.2f, внутри коробки %s", getBoxWeight(), whatInsideList);
        // (this.getClass() == "Apple") ? "яблоки" : "апельсины");
    }
}

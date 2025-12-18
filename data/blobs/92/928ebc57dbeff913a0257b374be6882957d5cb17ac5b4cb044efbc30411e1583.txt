public class Triangle extends Shape{
    private final String SOME_TEXT = "method printShape: I am Triangle, my color is  ";
    private final String TEXT = "I am Triangle, my color is  ";
    public Triangle(String colorName) {
        super(colorName);
    }

    @Override
    public void printShape() {
        System.out.println(SOME_TEXT + getColorName());
    }
    @Override
    public String toString() {
        return TEXT + getColorName();
    }

}

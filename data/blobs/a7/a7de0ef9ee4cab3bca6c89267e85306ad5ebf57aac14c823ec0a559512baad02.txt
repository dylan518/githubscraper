public class Module4Test {
    public static void main(String[] args) {
        
        Module4Rect module4Rect = new Module4Rect(10, 15);
        System.out.println("A rectangle has " + module4Rect.getNumSides() + " sides.");

        Module4Circ module4Circ = new Module4Circ(0);
        System.out.println("A circle has " + module4Circ.getNumSides() + " sides.");
    }
}

package one;

public class Pen extends WritingMaterials {
    private int countColor;
    private boolean auto;
    {
        countColor = 0;
        auto = false;
    }
    public Pen(){}
    public Pen(String name, String color, int price, double length, boolean draw, int countColor, boolean auto){
        super(name, color, price, length, draw=true);
        setCountColor(countColor);
        setAuto(auto);
    }

    public int getCountColor() {
        return this.countColor;
    }

    public void setCountColor(int countColor) {
        this.countColor = countColor;
    }

    public String getAuto() {
        return super.DaNet(this.auto);
    }

    public void setAuto(boolean auto) {
        this.auto = auto;
    }
    public void writeMyName(){
        System.out.println("Аня\n");
    }
    @Override
    public void display() {
        System.out.println("This is " + getClass().getName() + "\n");
        super.display();
        System.out.printf("Количество цветов: %s, Автоматическая: %s\n\n", getCountColor(),getAuto());
    }
}

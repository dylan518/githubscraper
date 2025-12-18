package RoadOther.Road19ReWork;

public class Rocket {
    private final String name;
    private final String number;
    private String color;
    private int hashcode;

    public Rocket (String name, String number, String color){
        this.name = name;
        this.number = number;
        this.color = color;
    }

    public void changeColor(String color){
        System.out.printf("Let's Rocket changing color begin!\nCurrent color: %s, Destination color: %s.\n", this.color, color);
        this.color = color;
        System.out.println("Done!");
    }

    @Override
    public int hashCode() {
        if (hashcode == 0) {
            hashcode = number.hashCode();
            hashcode += 31 * hashcode;
        }
        return hashcode;
    }
    @Override
    public boolean equals(Object obj) {
        if (obj == this) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Rocket rocket = (Rocket) obj;
        return number.equals(rocket.number) && name.equals(rocket.name);
    }

    @Override
    public String toString() {
        return "Rocket name is " + name + ". Number - " + number + ". Current color is " + color + '.';
    }
}

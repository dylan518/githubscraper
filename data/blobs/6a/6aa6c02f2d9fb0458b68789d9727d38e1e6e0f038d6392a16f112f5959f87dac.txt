package example24e;

public class Vehicle implements Comparable<Vehicle> {

    private String model;
    private int speed;

    public Vehicle(String model, int speed) {
        this.model = model;
        this.speed = speed;
    }

    @Override
    public String toString() {
        return "Vehicle{" +
                "model='" + model + '\'' +
                ", speed=" + speed +
                '}';
    }

    @Override
    public int compareTo(Vehicle other) {
        int base = this.model.compareTo(other.model);
        if (base != 0) {
            return base;
        }
        return this.speed - other.speed;
    }
}

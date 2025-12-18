package topshiriq3;

public class Car {
    private  int capacity;
    private  int oil;
    Car(Capacity capacity,Oil oil){
        this.capacity=capacity.getCapacity();
        this.oil=oil.getPetrol();

    }

    public int getCapacity() {
        return capacity;
    }

    public int getOil() {
        return oil;
    }
}

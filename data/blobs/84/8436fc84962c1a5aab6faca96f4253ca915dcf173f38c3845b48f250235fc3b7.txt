package Accessory;

public abstract class  Accessory {

    private final String name;
    private final int cost;

    public Accessory(String name, int cost){
        this.name=name;
        this.cost=cost;
    }


    public String getName() {
        return name;
    }

    public int getCost(){
        return cost;
    }

    @Override
    public String toString() {
        return "\n" + name + ':' +
                " cost=" + cost;
    }
}

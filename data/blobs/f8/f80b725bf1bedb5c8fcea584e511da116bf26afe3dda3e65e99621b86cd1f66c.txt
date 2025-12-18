package models.myobj;

public class MyObj {
    public Integer roll;
    public String name;

    public MyObj(Integer roll, String name) {
        this.roll = roll;
        this.name = name;
    }

    @Override
    public String toString() {
        return String.format("[%d, %s]", roll, name);
    }
}



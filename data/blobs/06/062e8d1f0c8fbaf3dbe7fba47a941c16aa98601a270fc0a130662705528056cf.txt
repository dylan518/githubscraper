package org.caselab.task3;

public final class Ship extends Vehicle implements IMechanicable {
    private final ShipEngine engine;

    public Ship(String name, int capacity, ShipEngine engine) {
        super(name, capacity);
        this.engine = engine;
    }

    @Override
    public void move() {
        try {
            this.engine.use();
            System.out.println(name + " is sailing on the sea.");

        }
        catch (RuntimeException e) {
            throw new RuntimeException(e);
        }

    }

    @Override
    public String toString() {
        return "Ship{" +
                "engine=" + engine +
                ", name='" + name + '\'' +
                ", wheels=" + wheels +
                ", capacity=" + capacity +
                '}';
    }

    @Override
    public ShipEngine getEngine() {
        return engine;
    }
}

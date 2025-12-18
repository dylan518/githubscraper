package com.epam.oops.terms.cohesion;

public class Main {
    public static void main(String[] args) {

        // low cohesion
        Car car = new Car();
        car.drive();
        car.performMaintenance();

        // high cohesion
        Driving driving = new Driving();
        Maintenance maintenance = new Maintenance();

        driving.drive();
        maintenance.performMaintenance();

    }
}


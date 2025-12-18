package com.example.springauto2.models;

public enum CarBodyType {
    Sedan("Sedan"),
    Limousine("Limousine"),
    Pickup("Pickup"),
    Hatchback("Hatchback"),
    StationWagon("StationWagon"),
    Liftback("Liftback"),
    Minivan("Minivan"),
    Coupe("Coupe"),
    Cabriolet("Cabriolet"),
    Roadster("Roadster"),
    Unclassified("Unclassified");


    private final String value;

    CarBodyType(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }
}

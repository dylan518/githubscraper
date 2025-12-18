package by.epam.lesson11.task10.enums;

public enum AircraftType {
    Airbus_A220("Airbus A220"),
    Boeing_737NG("Boeing 737NG"),
    Boeing_747("Boeing 747"),
    Boeing_777("Boeing 777")
    ;

    private final String aircraftType;

    AircraftType(String aircraftType) {
        this.aircraftType = aircraftType;
    }

    public String getAircraftType() {
        return aircraftType;
    }
}

package Vaccines;

import java.time.LocalDate;

public class Appointment {
    // I want this to return the local date and the appointment location
    // args = location (will be fed from patient)
    // date will come from the import
    // create them without a value 1st so that you can set in the next object
    protected LocalDate date;
    protected String location;

    public Appointment(LocalDate date, String location) {
        this.date = date;
        this.location = location;

    }
    public abstract String getDisplayText();
    @Override
    public String toString() {
        return date + " " + location;
    }

}

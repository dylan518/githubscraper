package com.neutrinosys.employees;

import java.time.LocalDate;

public class Weirdo {
    private String lastName;
    private String firstName;
    private LocalDate dob;

    public Weirdo(String lastName, String firstName, LocalDate dob) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.dob = dob;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public LocalDate getDob() {
        return dob;
    }

    public void setDob(LocalDate dob) {
        this.dob = dob;
    }
}

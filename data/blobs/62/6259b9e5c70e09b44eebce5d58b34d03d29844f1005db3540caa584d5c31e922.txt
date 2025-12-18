package com.besot.football.entities;

import com.besot.football.enums.Grade;

public class Staff extends User {
    private Grade grade;

    public Grade getGrade() {
        return grade;
    }

    public void setGrade(Grade grade) {
        this.grade = grade;
    }

    @Override
    public String toString() {
        return "Name: " + getName() + ", Age: " +getAge() + ", Sex: " + ", Identity Type: " +getIdtype()+ ", Phone No: "+ getPhoneNo() +", grade: " + grade ;
    }
}

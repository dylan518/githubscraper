package com.example.androiddiseasedetector;

import com.google.gson.annotations.SerializedName;

public class DiabetesRequest {
    @SerializedName("age")
    public float age;
    @SerializedName("sex")
    public float sex;
    
    @SerializedName("blood_pressure")
    public float blood_pressure;

    @SerializedName("cholestrol")
    public float cholestrol;
    
    @SerializedName("bmi")
    public float bmi;
    
    @SerializedName("smoker")
    public float smoker;
    
    @SerializedName("physical_activity")
    public float physical_activity;
    
    @SerializedName("fruits")
    public float fruits;
    
    @SerializedName("general_health")
    public float general_health;

    @SerializedName("mental_health")
    public float mental_health;

    @SerializedName("physical_health")
    public float physical_health;

    @SerializedName("education")
    public float education;

    @SerializedName("income")
    public float income;

    public DiabetesRequest() {

    }

//    public DiabetesRequest(float age, float sex, float blood_pressure, float cholestrol, float bmi, float smoker,
//                           float physical_activity, float fruits, float general_health, float mental_health,
//                           float physical_health, float education, float income) {
//        this.age = age;
//        this.sex = sex;
//        this.blood_pressure = blood_pressure;
//        this.cholestrol = cholestrol;
//        this.bmi = bmi;
//        this.smoker = smoker;
//        this.physical_activity = physical_activity;
//        this.fruits = fruits;
//        this.general_health = general_health;
//        this.mental_health = mental_health;
//        this.physical_health = physical_health;
//        this.education = education;
//        this.income = income;
//    }

    public void setAge(float age) {
        this.age = age;
    }

    public void setSex(float sex) {
        this.sex = sex;
    }

    public void setBlood_pressure(float blood_pressure) {
        this.blood_pressure = blood_pressure;
    }

    public void setCholestrol(float cholestrol) {
        this.cholestrol = cholestrol;
    }

    public void setBmi(float bmi) {
        this.bmi = bmi;
    }

    public void setSmoker(float smoker) {
        this.smoker = smoker;
    }

    public void setPhysical_activity(float physical_activity) {
        this.physical_activity = physical_activity;
    }

    public void setFruits(float fruits) {
        this.fruits = fruits;
    }

    public void setGeneral_health(float general_health) {
        this.general_health = general_health;
    }

    public void setMental_health(float mental_health) {
        this.mental_health = mental_health;
    }

    public void setPhysical_health(float physical_health) {
        this.physical_health = physical_health;
    }

    public void setEducation(float education) {
        this.education = education;
    }

    public void setIncome(float income) {
        this.income = income;
    }
}

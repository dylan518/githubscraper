package org.teaching.essential.lecture2_classes_p2.task3;

/*
Создать класс Машина с полями год(int), цвет(String).
Создать конструктор по умолчанию, конструктор с одним и 2-я параметрами.
Создать класс Main в котором создать экземпляры вызывая разные конструкторы.
 */

public class Car {

    private int yearProduction;
    private String color;

    public Car(){}

    public Car(int yearProduction){
        this.yearProduction = yearProduction;
    }

    public Car(int yearProduction, String color){
        this.yearProduction = yearProduction;
        this.color = color;
    }

    public int getYearProduction() {
        return yearProduction;
    }

    public String getColor() {
        return color;
    }
}

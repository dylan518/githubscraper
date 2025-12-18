package ua.hillel.hw8.pak0;

import ua.hillel.hw8.pak0.AbstractShape;

public class Circle extends AbstractShape {
    private double radius;

    public double squareFigures() {
        return Math.PI * Math.pow(radius, 2);
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    @Override
    public String toString() {
        return "Circle{" +
                "radius=" + radius +
                '}';
    }
}

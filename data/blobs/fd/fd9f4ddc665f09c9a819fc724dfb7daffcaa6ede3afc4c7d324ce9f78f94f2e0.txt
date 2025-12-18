package com.springCore.SpringExpLang;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
@Component
public class Demo {
    @Value("#{22+11}")
    private int x;
    //invoking the static method(calling the static method for injecting that value in your property)By Spel
    @Value("#{T(java.lang.Math).sqrt(25)}")
    private int y;
    //invoking the static Variable(calling the static variable for injecting that value in your property) by spel
    @Value("#{T(java.lang.Math).E}")
    private Double z;
    //creating the object for injecting that value in your property by Spel
    @Value("#{new java.lang.String('Anmol Pradhan')}")
    private String p;
    //For injecting the boolean type value in you property;
    @Value("#{8>3}")
    private Boolean isActive;

    @Override
    public String toString() {
        return "Demo{" +
                "x=" + x +
                ", y=" + y +
                ", z=" + z +
                ", p='" + p + '\'' +
                ", isActive=" + isActive +
                '}';
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public double getZ() {
        return z;
    }

    public void setZ(double z) {
        this.z = z;
    }

    public String getP() {
        return p;
    }

    public void setP(String p) {
        this.p = p;
    }

}
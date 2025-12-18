package com.aurionpro.model;

public class Child extends Parent {
    private  static int value;

    public Child(int value) {
        super(20);
        this.value = value;
        System.out.println("Inside Child");
    }

    @Override
    public String toString() {
        return "Child [value=" + value + "]";
    }
//  public  static int getValue() {
//       return value;
//    }
    public static  void printSuperValue() {
        System.out.println("Super value: " + getValue());
    }
}
	
	


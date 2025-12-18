package com.xworkz.datatypes.things;

public class WashingMachine {
	
	private String brand;
	private String type;
	private double capacity;

	public WashingMachine() {
		System.out.println("Created washing machine using no-arg const..");
	}

	public WashingMachine(String brand, String type, double capacity) {
		System.out.println("Created washing machine using string and double const..");
		this.brand=brand;
		this.type=type;
		this.capacity=capacity;
	}

	public void rinse() {
		System.out.println("Running rinse in washing machine");
	}

	public void show() {
		System.out.println("Washing machine name:"+brand);
		System.out.println("Washing machine type:"+type);
		System.out.println("Washing machine capacity:"+capacity);
	}


}

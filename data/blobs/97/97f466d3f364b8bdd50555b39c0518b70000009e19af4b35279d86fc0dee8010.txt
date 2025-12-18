package com.OOPs.Interface.SimpleExample;

public class Main {

	public static void main(String[] args) {
		//Creating an object of SmartLight class
		SmartDevice smartLight = new SmartLight();
		//Creating an object of SmartSecurity class
		SmartDevice smartSecurity = new SmartSecurity();
		
		// calling the method accessDevice in side the main method
		accessDevice(smartLight);
		accessDevice(smartSecurity);
	}
	
	// flexible code to access the methods
	public static void accessDevice(SmartDevice sd) {
		//Interface SmartDevice reference sd stores the objects of other classes and access the methods implemented
		sd.turnOn();
		sd.turnOff();
	}
}

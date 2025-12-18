package com.java.oops.examples;

public class ExInterface1Main implements ExInterface1  
{	
	@Override
	public void circle() // abstract method should be called if the interface is implemented to that particular class
	{
		System.out.println("This is circle - abstract method : " + (l+w)); // I can call final&static variable without creating object, if implemented	
	}
	
	void triangle() 
	{
		System.out.println("This is triangle - ExInterface1Main's own method");
	}
	
	public static void main(String[] args) 
	{
		// Scenario 1
		System.out.println("Class object");
		ExInterface1Main Obj = new ExInterface1Main();
		Obj.circle();				// abstract method
		Obj.square();				// default method
		ExInterface1.rectangle();	// static method can directly access from interface
		
		Obj.triangle(); 			// Own method 
		
		System.out.println();
		
		//Scenario 2
		// We can create object for interface, we can assign object variable to it, but can assign/implement the object
		System.out.println("Interface object");
		ExInterface1 iObj = new ExInterface1Main(); 
		
		iObj.circle();				// abstract method
		iObj.square();				// default method
		ExInterface1.rectangle();	// static method can directly access from interface
		
		// iObj.triangle(); - in here we can't call with interface object, were triangle method is from different class 
		// instead we can "cast" that method using interface object, like below example
		((ExInterface1Main) iObj).triangle();
	}


}

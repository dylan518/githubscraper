package com.moulik.inheritence;

public class OverridingDemo {

	public static void main(String[] args) {
		//Method Overriding is the concept in which the child class method overrides the parent class method.
		Bb b = new Bb();
		b.show(); //Show method from B is called even though show method is present in both classes.
		
	}

}
class Aa {
	int i;
	public void show() {
		i = 10;
		System.out.println("In A show");
	}
}

class Bb extends Aa {
	int i;
	public void show() {
		i = 20;
		System.out.println("In B show"+super.i);
		super.show();	//Super keyword can be used to call the parent class method here.
	}
}
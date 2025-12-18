package ytjava;

import ytjava.Outer.Inner;

class Outer1 {  //Outer.class
	static int a;

	public static void show() {
		System.out.println("Show method from Outer class");
	}

	static class Inner1 {    //Outer$Inner.class
		public void display() {
			System.out.println("display emthod from inner class");
		}
	}
}
public class OStaticInnerClass {

	// we can have varibales and methods
		public static void main(String[] args) {
			Outer1 obj = new Outer1();
			obj.show();

			//to create a static inner class object we have to use OuterClassname.InnerClassname
			Outer1.Inner1 obj1 = new Outer1.Inner1();
			obj1.display();
		}
}

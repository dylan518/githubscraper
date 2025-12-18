package gov.in.oupp.training.java.corejava.oops;

class A {
	int a,b;
	void show(){
		System.out.println("This is in class A");
	}
}
class B extends A{
	int c,d;
	void show(){
		System.out.println("This is in class B");
	}
		
}

public class InheritanceExample{
	public static void main(String[] args) {
		A obj=new A();
		B obj1=new B();
		obj.show();
		obj1.show();
	}
}

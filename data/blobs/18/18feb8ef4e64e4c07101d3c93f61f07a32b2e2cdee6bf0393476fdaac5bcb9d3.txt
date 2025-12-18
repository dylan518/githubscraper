package ch08.lecture.p03polymorphism;

public class C06Polymorphism {

	public static void main(String[] args) {
		MyInterface06 o1 = method1();

	}

	public static MyInterface06 method1() {
		return new MyClass06();
//		return new MyClass07(); 이것도 가능

	}

}

interface MyInterface06 {
}

class MyClass06 implements MyInterface06 {
}

class MyClass07 implements MyInterface06 {
}

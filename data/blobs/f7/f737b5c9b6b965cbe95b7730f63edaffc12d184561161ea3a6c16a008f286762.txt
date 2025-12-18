package org.staticToStatic;

public class StaticToStaticEx2 {
	    static int a,b;
		public static void test() {
			System.out.println("test method executed.");
		}
		public static void test1() {
			StaticToStaticEx2 obj=new StaticToStaticEx2();
			obj.a=50;
			a=60;
			obj.b=80;
			b=90;
			int c=obj.a+obj.b;
			int d=a+b;
			System.out.println("Addition of static variable : "+d);
			System.out.println("Addition : "+c);
			}
	public static void main(String[] args) {
		StaticToStaticEx2 obj1=new StaticToStaticEx2();
		obj1.test();	//by using object this is not correct way to call static method
		test();			//by direct calling
		obj1.test1();	// by using object this is not correct way to call static method
		test1();		//by direcrt call
		
	}

}

package oops.abstraction;

public class UseAbstractClass extends AbstractClass{

	@Override   // Annotation
	public void substraction(int a, int b) {
		System.out.println(a-b);		
	}
	
	public static void main(String[] args) {
		AbstractClass useABsCls = new UseAbstractClass();		
		useABsCls.addition(10, 20);
		useABsCls.substraction(10, 3);
	}

	

}

package This;
//Used to return the current class instance from the method
public class Test5 {
	
	Test5 m1()
	{
		return this;
	}

	public static void main(String[] args) {
		
		Test5 t = new Test5();
		t.m1();

	}

}

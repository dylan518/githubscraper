package OopsPart1;

public class FunctionMethod {

	public static void main(String[] args) {
		//Function and method both are same
		//Main method is starting point of execution
		
		FunctionMethod obj = new FunctionMethod();
		//obj is reference variable
		//new FunctionMethod(); is object
		//after creating object copy of all non static methods are given to this object
		//if you want to call non static methods you have to create object then only you will be able to call
		//why main method is void - because it will never return value
		obj.test();
		int j = obj.pqr();
		System.out.println(j);
		
		String k = obj.QA();
		System.out.println(k);
		
		int l = obj.division(20, 10);
		System.out.println(l);
		
		
	}
	public void test()//no input no output
	{
		System.out.println("Test Method");
	}
	//Return type = int
	public int pqr()//no input some output
	{
	System.out.println("Pqr Method");
	
	int a=10;
	int b=20;
	int c=a+b;
	return c;
	}
	
	//Return type = String
	public String QA()//no input some output
	{
		System.out.println("QA method");
		String s = "Selenium";
		return s;
	}
	
	//x,y input parameters and arguments
	public int division(int x,int y)
	{
		System.out.println("Devision method");
		int z = x/y;
		return z;
		
	}

}

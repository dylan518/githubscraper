class A
{
     private String s = "one";

     public void display()
	{
	  System.out.println("Two");
	}
	
    public void display(String s)
	{
	  System.out.println(s);
	}
}

public class Sona11 extends A
{
	
      protected String s = "one";    
      public static void main(String args[])
       {
	String s = "one";
		
	A a = new Sona11();
                	a.display();
	a.display("Three");
       }	
}

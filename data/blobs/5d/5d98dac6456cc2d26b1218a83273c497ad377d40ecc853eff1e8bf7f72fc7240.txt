package Inheritence1;

public class ShowChild extends ShowParent{
	
	public void child()
	{
		System.out.println("In Child Show");
	}
	
	

	public static void main(String[] args) {
	
		ShowChild obj=new ShowChild();
		obj.show();
		obj.child();
		
		

	}

}

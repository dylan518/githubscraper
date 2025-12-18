package ranjana;

public class Returntype {
	public void test() {// voidmeans it cant return a value
	int c = 10+20;
    System.out.println(c);
	}
	
	public int addition() {
		int d=30+40;
		System.out.println(d);
		String s="Velocity";
		System.out.println(s);
		return d;
		//return s; cannt write 2 return and string also cant return
	}
	
	public Returntype demo() {
		Returntype obj = new Returntype();
		obj.test();
		return obj;
	}
	
	public static void main (String [] args) {
	    Returntype obj= new Returntype();
	    //return obj;  void cant give return type
	    obj.addition();
	    obj.test();
	}
}

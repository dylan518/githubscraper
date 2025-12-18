class Oops{
	String name="";
	String jobrole="";
	int salary;
	
	public Oops(String x,String y){
		name=x;
		jobrole=y;
	}
	public Oops(){
    }
	public Oops(int z){
		 salary=z;
	}
	public static void main (String[] args){
		Oops obj=new Oops("shankar","intern");
		Oops obj1=new Oops(25000);
		System.out.println("name : "+obj.name);
		System.out.println("job role : "+obj.jobrole);
		System.out.println("salary : "+obj1.salary);
	}
}
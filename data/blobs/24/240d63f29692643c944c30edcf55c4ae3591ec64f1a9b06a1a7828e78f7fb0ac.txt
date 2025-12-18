package POJOforSerializationAndDeserialization;

public class EmployeeDetailsWithArray {
	//declare variable loclly
	String name;
	int empid;
	int[] phno;
	String[] email;
	String address;

	//create constructure for initilization
	public EmployeeDetailsWithArray(String name, int empid, int[] phno, String[] email, String address) {
		
		this.name = name;
		this.empid = empid;
		this.phno = phno;
		this.email = email;
		this.address = address;
	}
	
	//getters methods
	public String getName() {
		return name;
	}
	public int getEmpid() {
		return empid;
	}
	public int[] getPhno() {
		return phno;
	}
	public String[] getEmail() {
		return email;
	}
	public String getAddress() {
		return address;
	}
	
}

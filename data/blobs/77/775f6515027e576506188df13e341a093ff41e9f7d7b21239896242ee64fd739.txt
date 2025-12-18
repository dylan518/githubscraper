package org.encapsulation;



class Employee {

	private String employeeId;
	private String employeeName;
	private int salary;
	private int bonus;
	private int jobLevel;
	
	public String getemployeeId(){
	    return employeeId;
	}
	public void setemployeeId( String employeeId){
	    this.employeeId=employeeId;
	}
	    
	
	public String getemployeeName(){
	    return employeeName;
	    
	}
	public void setemployeeName( String employeeName){
	    this.employeeName=employeeName;
	}
	public int getsalary(){
	    return salary;
	}
	public void setsalary( int salary){
	    this.salary=salary;
	}
	public int getbonus(){
	    return bonus;
	}
	public void setbonus(int bonus){
	    this.bonus=bonus;
	}
	public int getjobLevel(){
	    return jobLevel;
	}
	public void setjobLevel( int jobLevel){
	    this.jobLevel=jobLevel;
	}

	public void calculateSalary() {
		if (this.jobLevel >= 4) {
			this.bonus = 100;
		} else {
			this.bonus = 50;
		}
		this.salary += this.bonus;
	}
}

class EncapExercise {

	public static void main(String args[]) {

		Employee employee = new Employee();
		
		employee.setemployeeId("C101");
		employee.setemployeeName("Steve");
		employee.setsalary(650);
		employee.setjobLevel(4);

		employee.calculateSalary();

		System.out.println("Employee Details");
		System.out.println("Employee Id: " + employee.getemployeeId());
		System.out.println("Employee Name: " + employee.getemployeeName());
		System.out.println("Salary: " + employee.getsalary());

	}
}
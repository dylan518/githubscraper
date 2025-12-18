package vw.him.springcontainer.di.model;

import java.util.Objects;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component("emp1")
public class Emp implements Comparable<Emp>{
	
	
	
	private int empId;
	private String empName;
	private double empSalary;
	
//	@Autowired
	private Dept dept;
	
	public Emp() {
		System.out.println("0 arg constructor Emp called!");
	}
	
	@Autowired
	public Emp(@Value("${employee.id}")int empid,
			   @Value("${employee.name}") String name,
			   @Value("${employee.salary}") double salary,
			   Dept dept)
	{
		this.empId=empid;
		this.empName=name;
		this.empSalary=salary;
		this.dept=dept;
	}
			
	
//	public Emp(int empId, String empName, double empSalary, Dept dept) {
//		super();
//		this.empId = empId;
//		this.empName = empName;
//		this.empSalary = empSalary;
//		this.dept = dept;
//	}


	public int getEmpId() {
		return empId;
	}

	public void setEmpId(int empId) {
		this.empId = empId;
	}


	public String getEmpName() {
		return empName;
	}

	public void setEmpName(String empName) {
		this.empName = empName;
	}
	public double getEmpSalary() {
		return empSalary;
	}

	public void setEmpSalary(double empSalary) {
		this.empSalary = empSalary;
	}

	public Dept getDept() {
		return dept;
	}

	public void setDept(Dept dept) {
		this.dept = dept;
	}
	
	public double computeAnnualSalary() {
		return this.empSalary*12;
	}

	@Override
	public String toString() {
		return "Emp [empId=" + empId + ", empName=" + empName + ", empSalary=" + empSalary + ", dept=" + dept + "]";
	}

	

	@Override
	public int compareTo(Emp o) {
		return this.empId - o.getEmpId();
	}
	
	

}

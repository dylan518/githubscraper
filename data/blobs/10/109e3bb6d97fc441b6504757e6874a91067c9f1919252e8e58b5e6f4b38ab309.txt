package com.demo.model;


import javax.persistence.*;

@Entity
@Table(name="Employees")
public class Employee {
	private int eid;
	private String ename;
	private int deptid;
	
	@JoinTable(name="emp_proj11")
	private Department dept;
	
	
	public Employee() {
		super();
		
	}
	public Employee(int eid, String ename, int deptid, Department dept) {
		super();
		this.eid = eid;
		this.ename = ename;
		this.deptid = deptid;
		this.dept = dept;
	}
	public int getEid() {
		return eid;
	}
	public void setEid(int eid) {
		this.eid = eid;
	}
	public String getEname() {
		return ename;
	}
	public void setEname(String ename) {
		this.ename = ename;
	}
	public int getDeptid() {
		return deptid;
	}
	public void setDeptid(int deptid) {
		this.deptid = deptid;
	}
	public Department getDept() {
		return dept;
	}
	public void setDept(Department dept) {
		this.dept = dept;
	}
	@Override
	public String toString() {
		return "Employee [eid=" + eid + ", ename=" + ename + ", deptid=" + deptid + ", dept=" + dept + "]";
	}
	
}

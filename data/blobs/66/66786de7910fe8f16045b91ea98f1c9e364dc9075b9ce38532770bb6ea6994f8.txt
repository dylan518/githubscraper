package com.telusko.entity;

import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;

@Entity
public class Department 
{
	@Id
    private String depId;
	
	private String name;
	
	@OneToMany(cascade=CascadeType.ALL)
	private Set<Employee> employee;
	
	public Department()
	{
		System.out.println("Depart zero param Constructor for hibernate");
	}

	@Override
	public String toString() {
		return "Department [depId=" + depId + ", name=" + name + ", employee=" + employee + "]";
	}

	public String getDepId() {
		return depId;
	}

	public void setDepId(String depId) {
		this.depId = depId;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Set<Employee> getEmployee() {
		return employee;
	}

	public void setEmployee(Set<Employee> employee) {
		this.employee = employee;
	}
	
	
	
}

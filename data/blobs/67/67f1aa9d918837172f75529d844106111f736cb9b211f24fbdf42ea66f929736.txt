package com.example.demo;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import jakarta.servlet.http.HttpSession;

@Controller
public class EmployeeController {
	
	@Autowired
	EmployeeRepo repo;
	
	@RequestMapping("main")
	String welcome() {
		return "Welcome.jsp";
	}
	
	@RequestMapping("addEmp")
	String addEmp(Employee e,HttpSession h1 ) {
		repo.save(e);
		h1.setAttribute("msg", e.getEname()+" had been added into Db...!!!!");
		return "AddEmply.jsp";
		
	}
	
	@RequestMapping("removeEmp")
	String removeEmp(String eid,HttpSession h1 ) {
		Employee e=repo.findById(eid).orElse(null);
		if(e!=null) {
			repo.deleteById(eid);  
			h1.setAttribute("value",e.getEname()+" had been removed....!!!");
		}
		else {
			h1.setAttribute("value","Invalid Eid .....!!!!!");
		}
		return "RemoveEmp.jsp";
		
	}
	
	@RequestMapping("EmpById")
	String empById(String eid ,HttpSession h1) {
		Employee e=repo.findById(eid).orElse(null);
		if(e!=null) { 
			h1.setAttribute("info",e);
		}
		else {
			h1.setAttribute("info","Invalid Eid .....!!!!!");
		}
		return "EmplyById.jsp";
	}
	
	@RequestMapping("EmpByAge")
	String empByAge(int age ,HttpSession h1) {
		List<Employee> l1=repo.findByAge(age);
		if(l1.size()==0) {
			h1.setAttribute("info","Employees Not Found.....!!");
		}
		else {
			h1.setAttribute("info", l1);
		}
		return "FindByAge.jsp";
	}
	
	@RequestMapping("EmpByAgeBW ")
	String empByAgeBw(int age1,int age2 ,HttpSession h1) {
		List<Employee> l1=repo.findByBwAge(age1,age2);
		if(l1.size()==0) {
			h1.setAttribute("info","Employees Not Found.....!!");
		}
		else {
			h1.setAttribute("info", l1);
		}
		return "FindByAgeBw.jsp";
	}
	
	@RequestMapping("EmpByEmailOrEid")
	String empByEmailOrEid(String value,HttpSession h1) {
		Employee e=repo.findByEidOrEmail(value, value);
		if(e!=null) {
			h1.setAttribute("info", e);
		}
		else {
			h1.setAttribute("info","Employees Not Found.....!!");
		}
		return "EmpByEmailOrEid.jsp";
	}
	
	

	
}

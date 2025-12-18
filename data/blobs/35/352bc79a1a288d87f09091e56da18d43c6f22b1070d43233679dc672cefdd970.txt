package com.fbla.student.bo;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.fbla.student.dal.ClassDAO;
import com.fbla.student.model.SchoolClass;

@Component
public class SchoolClassBo {
	
	@Autowired
	private ClassDAO classdao;
	
	public String addClass(int userId, int classId) {
		return classdao.addClass(userId, classId);
	}
	
	public List<SchoolClass> getAllClasses(){
		return classdao.getAllClasses();
	}
	
	public List<SchoolClass> getClasses(int userId){
		return classdao.getClasses(userId);
	}
}

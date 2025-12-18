package com.springtutorial.withoutxml;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
//@ComponentScan(basePackages="com.springtutorial.withoutxml")
public class config {

	@Bean
	public Student createstudent() {
		return new Student();
	}
	
	@Bean
	public Courses createcourse() {
		return new Courses();
	}
	
	@Bean
	public List<String> storesubject() {
		List<String> s = Arrays.asList("CS","EXTC");
		return s;
	}
	
	@Bean
	public Teacher storeTeacher() {
		Teacher t = new Teacher();
		t.setTid(101);
		t.setTname("Himal");
		return t;
	}
	
	@Bean
	public List<Friends> storeFriends() {
		List<Friends> f = new ArrayList<Friends>();
		f.add(new Friends(101, "Dagadu"));
		f.add(new Friends(102, "Viaml"));
		f.add(new Friends(103, "Bharati"));
		return f;
	}

}

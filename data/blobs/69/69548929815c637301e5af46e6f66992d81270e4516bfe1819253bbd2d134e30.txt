package com.kodnest.main;

import org.springframework.context.support.ClassPathXmlApplicationContext;

import com.kodnest.bean.Trainer;
import com.kodnest.bean.University;

public class App {

	public static void main(String[] args) {
		ClassPathXmlApplicationContext c = new ClassPathXmlApplicationContext("applicationcontext.xml");
//		Trainer tr = (Trainer) c.getBean("trainer");
//		System.out.println(tr);
		University un = (University) c.getBean("u");
		System.out.println(un);
	}

} 

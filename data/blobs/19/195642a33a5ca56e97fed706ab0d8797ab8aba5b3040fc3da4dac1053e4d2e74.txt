package com.collections.comparable;

import java.util.ArrayList;
import java.util.Collections;

class Student implements Comparable<Student>{
	int id;
	String name;
	int age;
	Student(int id,String name,int age){
	this.id = id;
	this.name = name;
	this.age = age;	
	}
@Override
public int compareTo(Student st) {
	if(age == st.age)
		return 0;
	else
		if(age > st.age)
	return 1;
		else
		return -1;
            }	
}

public class TestComparable {
	public static void main(String[] args) {
	ArrayList<Student> al = new ArrayList<Student>();
	al.add(new Student(101,"Abhay",23));
	al.add(new Student(106,"Aayush",22));
	al.add(new Student(109,"Mishra",26));		
	Collections.sort(al);
	for(Student st:al) {
	System.out.println(st.id + " " + st.name + " " +st.age);
	}
	}
}




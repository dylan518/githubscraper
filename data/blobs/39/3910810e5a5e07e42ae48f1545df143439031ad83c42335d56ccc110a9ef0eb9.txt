package arrayinjava;

import java.util.Scanner;

public class Stud {
	
	int id,marks;
	String name;
	
	Stud(int id,String name,int marks)
	{
		this.id=id;
		this.name=name;
		this.marks=marks;
	}
	
	public String toString()
	{
		return id+" "+name+" "+marks;
	}

	
	}


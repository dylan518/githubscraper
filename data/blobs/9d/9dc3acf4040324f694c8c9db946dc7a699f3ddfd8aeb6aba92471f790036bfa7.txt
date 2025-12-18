package prepare.tutorials.thirtyDaysOfCode.day12_Inheritance;

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    	String firstName, lastName;
    	int idNumber, scoreQuantity;
    	int[] testScores;
    	try(Scanner scanner = new Scanner(System.in)) {
            firstName=scanner.next();
            lastName=scanner.next();
            idNumber=scanner.nextInt();
            scanner.nextLine();
            scoreQuantity=scanner.nextInt();
            testScores=new int[scoreQuantity];
            scanner.nextLine();
            for(int i=0; i<scoreQuantity; i++) {
            	testScores[i]=scanner.nextInt();
            }
        }
    	Student student = new Student(firstName, lastName, idNumber, testScores);
    	System.out.println(student);
    }
}

class Student extends Person {
	int[] testScores;

	Student(String firstName, String lastName, int idNumber, int[] testScores) {
		super(firstName, lastName, idNumber);
		this.testScores=testScores;
	}

	public int getAvgTestScores() {
		int sum=0;
		for(int score : testScores) {
			sum+=score;
		}
		return sum/testScores.length;
	}

	public String getGrade() {
		int avgScore=getAvgTestScores();
		return avgScore<=100 && avgScore>=90 ? "O" : avgScore>=80 ? "E" : avgScore>=70 ? "A" : avgScore>=55 ? "P" : avgScore>=40 ? "D" : "T";
	}

	@Override
	public String toString() {
		String newLine=System.getProperty("line.separator");
		return "Name: " + lastName + ", " + firstName + newLine + "ID: " + idNumber + newLine + "Grade: " + getGrade();
	}


}

class Person {
	protected String firstName;
	protected String lastName;
	protected int idNumber;

	Person(String firstName, String lastName, int idNumber) {
		this.firstName=firstName;
		this.lastName=lastName;
		this.idNumber=idNumber;
	}

	public String getFirstName() {
		return firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public int getIdNumber() {
		return idNumber;
	}

	@Override
	public String toString() {
		return "Person [firstName=" + firstName + ", lastName=" + lastName + ", idNumber=" + idNumber + "]";
	}
}

//enum Grade {
//	O, E, A, P, D, T;
//	/*
//	Grade(String grade) {
//		super(grade);
//	}
//	*/
//}
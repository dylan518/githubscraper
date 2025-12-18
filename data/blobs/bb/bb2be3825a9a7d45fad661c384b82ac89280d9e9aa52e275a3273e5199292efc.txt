package com.syntax.class16;

public class Students {
    String name;
    int id;
    static int numberOfStudents=0;

    public static void main(String[] args) {
        Students a=new Students();
        Students b=new Students();
        Students c=new Students();
        a.name="Igor";
        a.id=11;
        numberOfStudents+=1;
        b.name="Kat";
        b.id=12;
        numberOfStudents+=1;
        c.name="Jose";
        c.id=13;
        numberOfStudents+=1;
        System.out.println("Total number of students is: "+numberOfStudents);
    }
}

package com.company.Pojo;

public class Student{
    private int rollNo;
    private String Name;

    public Student(int rollNo, String name) {
        this.rollNo = rollNo;
        Name = name;
    }

    public Student() {

    }

    public int getRollNo() {
        return rollNo;
    }

    public void setRollNo(int rollNo) {
        this.rollNo = rollNo;
    }

    public String getName() {
        return Name;
    }

    public void setName(String name) {
        Name = name;
    }

    @Override
    public String toString() {
        return "Student{" +
                "rollNo=" + rollNo +
                ", Name='" + Name + '\'' +
                '}';
    }

//    @Override
//    public int compareTo(Student o) {
//        return this.getRollNo()-o.getRollNo();
//    }
}

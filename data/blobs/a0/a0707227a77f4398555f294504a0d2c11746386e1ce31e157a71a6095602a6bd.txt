package com.bootcampexercise.Module10.Activity1and2and4;

public class Employee extends Person {
    private String jTitle;
    private String company;
    private int salary = 0;

    public Employee() {
    }

    public Employee(String jTitle, String company, int salary) {
        this.jTitle = jTitle;
        this.company = company;
        this.salary = salary;
    }

    public String getjTitle() {
        return jTitle;
    }

    public void setjTitle(String jTitle) {
        this.jTitle = jTitle;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public void introduce(String name, int age) {
        if (jTitle == null && company == null && salary == 0) {
            System.out.println("My name is " + name + " and I am " + age + " years old.");
        } else {
            System.out.println("My name is " + name + " and I am " + age + " years old.\n I am working as " + jTitle +
                    " in \"" + company + "\" and my salary is " + salary);

        }
    }

    public static String getHighestPaidEmp(EmployeeList list1) {
        Employee emp;
        int sal1 = list1.employees.get(0).getSalary();
        String jTittle1 = list1.employees.get(0).getjTitle();

        for (int i = 1; i < list1.employees.size(); i++) {
            emp = list1.employees.get(i);
            if (sal1 < emp.getSalary())
            {    sal1 = list1.employees.get(i).getSalary();
                 jTittle1 = list1.employees.get(i).getjTitle();
            }

        }
        return jTittle1;

    }
}
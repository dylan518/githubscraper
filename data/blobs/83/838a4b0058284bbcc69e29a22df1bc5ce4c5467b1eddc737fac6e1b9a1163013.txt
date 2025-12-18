package studentDatabaseApp;

import java.util.Scanner;

public class Student {
    private String firstName;
    private String lastName;
    private int year;
    private String studentID;
    private String courses = "";
    private int tuitionBalance = 0;
    private static int costOfCourse = 600;
    private static int id = 1000;


    // Constructor: prompt user to enter student's name and year
    public Student(){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter student's first name: ");
        this.firstName = sc.nextLine();

        System.out.print("Enter student's last name: ");
        this.lastName = sc.nextLine();

        System.out.print("Enter student's year: ");
        this.year = sc.nextInt();

        setStudentID();

    }

    // Generate ID
    private void setStudentID(){
        //Year + ID
        id++;
        studentID = year + "" + id;
    }

    // Enroll in courses
    public void enroll() {
        //Get inside a loop
        do {
            System.out.print("Enter course to enroll (Q to quit): ");
            Scanner sc = new Scanner(System.in);
            String course = sc.nextLine();
            if (!course.equals("Q")){
                courses = courses + "\n  " + course;
                tuitionBalance = tuitionBalance + costOfCourse;
            } else
                break;
    }while (1!=0); //For Infinite loop condition


    }
    // View Balance
    public void viewBalance(){
        System.out.println("Your Tuition Balance is: Rs. " + tuitionBalance);
    }

    // Pay Tuition
    public void payTuition(){
        viewBalance();

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Payment: ");
        int payment = sc.nextInt();
        tuitionBalance = tuitionBalance - payment;
        System.out.println("Thank you for your payment of Rs. " + payment);

    }

    // Show Status
    public String showInfo(){
        return "Name: " + firstName + " " + lastName +
                "\nYear: " + year +
                "\nStudent ID: " + studentID +
                "\nCourses Enrolled In: " + courses +
                "\nTuition Balance: Rs. " + tuitionBalance;
    }
}

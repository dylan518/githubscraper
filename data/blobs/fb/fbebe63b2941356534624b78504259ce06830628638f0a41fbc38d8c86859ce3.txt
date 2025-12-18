package Assignments;

public class Assignment6_Employee {
    long employeeId;
    String employeeName;
    String employeeAddress;
    long employeePhone;
    double basicSalary;
    double specialAllowance=250.80;
    double hra=1000.50;
    Assignment6_Employee(){
        System.out.println("Please provide employee details");//no-args constructor
    }
    Assignment6_Employee(long id, String name, String address, long phone){
        employeeId=id;
        employeeName=name;
        employeeAddress=address;
        employeePhone=phone;
    }
    public double basicSalary(double basicSalary) {
        double salary=basicSalary+((basicSalary/specialAllowance)*100)+((basicSalary/hra)*100);
        return salary; 
    }
}

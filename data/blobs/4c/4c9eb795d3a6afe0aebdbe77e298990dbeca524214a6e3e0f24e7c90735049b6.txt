package basics;
public class Test {
    public static void main(String[] args) {
        Teacher hourlyTeacher = new HourlyBased(1, "AJ", "1234567890", 50, 40);
        Teacher salaryTeacher = new SalaryBased(2, "AB", "2222222222", 3000);

        hourlyTeacher.salary();
        salaryTeacher.salary();
    }
}

abstract class Teacher {
    int Tid;
    String Tname;
    String MobileNo;

    Teacher(int Tid, String Tname, String MobileNo) {
        this.Tid = Tid;
        this.Tname = Tname;
        this.MobileNo = MobileNo;
    }
    abstract void salary();
}
class HourlyBased extends Teacher {
    double rateperhr;
    int hrs;

    HourlyBased(int Tid, String Tname, String MobileNo, double rateperhr, int hrs) {
        super(Tid, Tname, MobileNo);
        this.rateperhr = rateperhr;
        this.hrs = hrs;
    }

    @Override
    void salary() {
        double totalSalary = rateperhr * hrs;
        System.out.println("Hourly Based Teacher Salary: " + totalSalary);
    }
}

class SalaryBased extends Teacher {
    int salary;

    SalaryBased(int Tid, String Tname, String MobileNo, int salary) {
        super(Tid, Tname, MobileNo);
        this.salary = salary;
    }
    @Override
    void salary() {
        System.out.println("Salary Based Teacher Salary: " + salary);
    }
}


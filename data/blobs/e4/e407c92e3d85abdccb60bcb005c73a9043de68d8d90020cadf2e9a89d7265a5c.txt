package Q8Polymorphism;

public class Manager extends Employee{

    @Override
    public void Manager() {
        System.out.println("Manager's Salary: $50000/Year");
    }

    @Override
    public void Programmer() {
        System.out.println("Programmer's Salary: $60000/Year");
    }

    public static void main(String[] args) {
        Manager m = new Manager();
        m.calculateSalary("Salary for this Department:");
        m.Manager();
        m.Programmer();
    }
}

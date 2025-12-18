package ExercicioPoo01;

public class Employee {
    String name;
    double groossSalary;
    double tax;

    public double netSalary(){
        return groossSalary - tax;
    }

    public void increaseSalary(double percentage){
        groossSalary += groossSalary * percentage / 100.0;
    }

    public String toString() {
        return name + ", $ " + String.format("%.2f", netSalary());
    }



}

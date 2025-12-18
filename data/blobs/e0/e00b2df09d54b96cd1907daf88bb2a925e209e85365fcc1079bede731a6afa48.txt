package oops;


import java.util.Date;

public class ShiftSupervisor extends Employee{
    private double bonus;
    private double annualSalary;
    private boolean isGoalMet;

    public ShiftSupervisor(){}

    public ShiftSupervisor(double bonus, double annualSalary){
        this.bonus = bonus;
        this.annualSalary=annualSalary;
    }

    public ShiftSupervisor(String name, String employeeNumber,
                           Date hireDate, double bonus, double annualSalary) {
        super(name, employeeNumber, hireDate);
        this.bonus = bonus;
        this.annualSalary = annualSalary;
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public double getAnnualSalary() {
        return annualSalary;
    }

    public void setAnnualSalary(double annualSalary) {
        this.annualSalary = annualSalary;
    }

    public boolean isGoalMet() {
        return isGoalMet;
    }

    public void setGoalMet(boolean goalMet) {
        isGoalMet = goalMet;
    }


    @Override
    public String toString() {
        return "ShiftSupervisor{" +
                "bonus=" + bonus +
                ", annualSalary=" + annualSalary +
                ", isGoalMet=" + isGoalMet +
                '}';
    }
}

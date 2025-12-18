package org.example.classes;

public class OnlineWorker extends Worker {
    private static final double internet = 15;

    public OnlineWorker (String name, String surname, double priceHour) {
        super(name, surname, priceHour);
    }

    @Override
    public double calculateSalary(int hoursWorked) {
        return super.calculateSalary(hoursWorked) + internet;
    }
    
    @Deprecated
    public double calculateSalaryNoInternet(int hoursWorked){
        return super.calculateSalary(hoursWorked);
    }
}

import java.util.ArrayList;
import java.util.List;

public class Player {
    String name;
    Skills skills;
    Project project;
    public double money;
    public List<Subcontractors> subcontractorsList = new ArrayList<>();
    public List<Employee> employees;
    public Player(String name, Skills skills, double money) {
        this.name = name;
        this.skills = skills;
        this.money = money;
        this.employees = new ArrayList<>();
    }
    public Project getProject() {
        return project;
    }
    public void ifComplexProject(Project project) {
        if(getProject().getDifficulty().equals("complex")) {
            double temp = project.getPrice();
            temp = temp/2;
            money = temp+money;
            project.setPrice(temp);
        }
    }

    public double getMoney() {
        return money;
    }

    public void setMoney(double money) {
        this.money = money;
    }
    public void payment() {
        if (getMoney() >= employees.size() * 10) {
            double mon = getMoney();
            mon -= employees.size() * 10;
            setMoney(mon);
        } else {
            System.out.println("Not enough money to pay employees");
        }
    }
    public void hireSubcontractor(Subcontractors subcontractors){
        subcontractorsList.add(subcontractors);
        this.money -= subcontractors.price;
    }
    public void hireEmployee(Employee employee) {
        if(employee.getSalary()<= getMoney())
            employees.add(employee);
        this.money -= employee.getSalary();
    }
    public void fireEmployee(Employee employee) {
        employees.remove(employee);
        this.money -= 1000.00;
    }

    @Override
    public String toString() {
        return "Player{" +
                "name='" + name + '\'' +
                ", money=" + money +
                ", subcontractors=" + subcontractorsList +
                '}';
    }
    public boolean hasSalespearson(List<Employee> employees){
        if (employees == null) {
            return false;
        }
        for(Employee employee : employees) {
            if(employee instanceof Salespearson){
                return true;
            }
        }
        return false;
    }

}

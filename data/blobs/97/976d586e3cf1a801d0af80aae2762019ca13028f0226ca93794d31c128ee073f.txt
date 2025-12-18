
public class Main {

  static Employee[] employees;

  public static void main(String[] args) {
    employees = new Employee[10];
    employees[0] = new Employee("Артемович Артем Артемов", 3, 39000);
    employees[1] = new Employee("Владмировский Владимир Владимирович", 3, 13000);
    employees[2] = new Employee("Светланова Света Светланова", 4, 23000);
    employees[3] = new Employee("Маринова Марина Мариновна", 4, 32000);
    employees[4] = new Employee("Олегов Олег Олегович", 2, 33000);
    employees[5] = new Employee("Никитин Никита Никитич", 2, 35000);
    employees[6] = new Employee("Анольев Анатолий Анатольевич", 2, 33000);
    employees[7] = new Employee("Семенович Семен Семенов", 5, 100000);
    employees[8] = new Employee("Иванов Иван Иванович", 4, 70000);
    employees[9] = new Employee("Петров Петр Петрович", 1, 53000);

    fullName();
    allInform();
    totalSalaryPerMonth();
    minAndMaxSalary();
    averageSalary();
  }

  public static void fullName() {

    for (int i = 0; i < employees.length; i++) {
      System.out.println(employees[i].getFullName());
    }
  }

  public static void allInform() {
    for (int i = 0; i < employees.length; i++) {
      System.out.println(employees[i].toString());
    }
  }

  public static int totalSalaryPerMonth() {
    int totalsolary = 0;
    for (int i = 0; i < employees.length; i++) {
      totalsolary = totalsolary + employees[i].getSalary();

    }
    System.out.println(" Общая сумма затрат на заработную плату - " + totalsolary);
    return totalsolary;
  }

  public static void minAndMaxSalary() {
       int minSalary = employees[0].getSalary();
       int maxSalary = employees[0].getSalary();
       String maxSalaryEmp = "";
       String minSalaryEmp = "";


    for (int i = 0; i<employees.length; i++){
      if (minSalary<employees[i].getSalary()){
         minSalary=employees[i].getSalary();
         minSalaryEmp = employees[i].getFullName();
      } else if (maxSalary > employees[i].getSalary()) {
        maxSalary=employees[i].getSalary();
        maxSalaryEmp=employees[i].getFullName();

      }


    }
    System.out.println("Максимальная зарплата " + minSalary + minSalaryEmp);
    System.out.println("Минимальная  зарплата " + maxSalary + maxSalaryEmp);
  }
  public  static void averageSalary(){
    int totalsolary = totalSalaryPerMonth();
    totalsolary = totalsolary / employees.length;
    System.out.println("Среднее значение зарплат - " +  totalsolary);

  }
}


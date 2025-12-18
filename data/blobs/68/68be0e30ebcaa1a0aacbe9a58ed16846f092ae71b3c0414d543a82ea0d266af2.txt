package JAVA_08;

import java.util.*;
import java.util.stream.Collectors;

public class Empl_Class_Stream {

    private int id;
    private String name;
    private int age;
    private String gender;
    private String department;
    private int yearPassing;
    private double salary;

    public Empl_Class_Stream() {
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public int getYearPassing() {
        return yearPassing;
    }

    public void setYearPassing(int yearPassing) {
        this.yearPassing = yearPassing;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    @Override
    public String toString() {
        return "Stream_Empl_Class{" + "id=" + id + ", name='" + name + '\'' + ", age=" + age + ", gender='" + gender + '\'' + ", department='" + department + '\'' + ", yearPassing=" + yearPassing + ", salary=" + salary + '}';
    }

    public Empl_Class_Stream(int id, String name, int age, String gender, String department, int yearPassing, double salary) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.department = department;
        this.yearPassing = yearPassing;
        this.salary = salary;
    }

    public static void main(String[] args) {
//        @***
        List<Empl_Class_Stream> empList = new ArrayList<Empl_Class_Stream>();
        empList.add(new Empl_Class_Stream(1, "ganesha", 11, "male", "arts", 2000, 150000));
//        empList.add(new Stream_Empl_Class(1,"ganesha",11,"male","arts",2000,150000));

        empList.add(new Empl_Class_Stream(2, "shubham", 24, "male", "commerce", 2002, 140000));
        empList.add(new Empl_Class_Stream(3, "akash", 24, "male", "engineering", 2003, 130000));
        empList.add(new Empl_Class_Stream(4, "vijay", 22, "male", "architecture", 2023, 120000));
        empList.add(new Empl_Class_Stream(5, "vaishnavi", 23, "female", "architecture", 2022, 110000));
        empList.add(new Empl_Class_Stream(6, "nishchay", 20, "male", "electrical", 2024, 100000));
        empList.add(new Empl_Class_Stream(7, "prashant", 27, "male", "computer", 2016, 900000));
        empList.add(new Empl_Class_Stream(8, "supriya", 12, "female", "civil", 2021, 800000));
        empList.add(new Empl_Class_Stream(9, "hanuman", 14, "male", "natural", 2005, 700000));
        empList.add(new Empl_Class_Stream(10, "saurabh", 25, "male", "science", 2020, 600000));
        empList.add(new Empl_Class_Stream(11, "Bharat", 30, "male", "architecture", 2030, 550000));
//        empList.add(new Stream_Empl_Class(7,"prashant",27,"male","computer",2016,900000));


//  Que How many male and female employees are there in the organization?


     /*  List<Stream_Empl_Class> noOfMaleFemaleEmp  =empList.stream()
               .collect(Collectors.groupingBy(Stream_Empl_Class::getGender,Collectors.counting()));
        System.out.println(noOfMaleFemaleEmp);*/


//   Que    Print the name of all departments in the organization?
//        empList.stream().map(Stream_Empl_Class::getDepartment).forEach(System.out::println);

//   Que   What is the average age of male and female employees?

      /*Map<String,Double> m1=
               empList.stream()
              .collect(Collectors.groupingBy(Stream_Empl_Class::getGender,Collectors.averagingInt(Stream_Empl_Class::getAge)));
        System.out.println(m1);*/

//   Que Get the details of highest paid employee in the organization?
        /*Optional<Stream_Empl_Class> op1 = empList.stream().collect(Collectors.maxBy(Comparator.comparingDouble(Stream_Empl_Class::getSalary)));
        Stream_Empl_Class highestPaidEmployee = op1.get();
        System.out.println("Details of highest paid employee");
        System.out.println("id "+highestPaidEmployee.getId());
        System.out.println("name "+highestPaidEmployee.getName());
        System.out.println("age "+highestPaidEmployee.getAge());
        System.out.println("gender "+highestPaidEmployee.getGender());
        System.out.println("department "+highestPaidEmployee.getDepartment());
        System.out.println("YearPassing "+highestPaidEmployee.getYearPassing());
        System.out.println("highest salary "+highestPaidEmployee.getSalary());*/


//   Que Get the names of all employees who have joined after 2010?
       /* empList.stream().filter(f->f.getYearPassing() >2020).map(Stream_Empl_Class::getName)
                .forEach(System.out::println);*/

//   Que Count the number of employees in each department?
//        Map<String,Long> number_emp = empList.stream().collect(Collectors.groupingBy(Stream_Empl_Class::getDepartment,Collectors.counting()));
//        System.out.println("number of emp in department "+number_emp);


//  Que  What is the average salary of each department?
//        Map<String , Double > average_salaryDep = empList.stream().collect(Collectors.groupingBy(Stream_Empl_Class::getDepartment,Collectors.averagingDouble(Stream_Empl_Class::getSalary)));
//        System.out.println(average_salaryDep);

//  Que  Get the details of youngest male employee in the product development department?
//        Optional <Stream_Empl_Class> youngestEmp = empList.stream().filter(e -> e.getGender()=="male"&&e.getDepartment()=="architecture")
//                .min(Comparator.comparingInt(Stream_Empl_Class::getAge));
//        Stream_Empl_Class young = youngestEmp.get();
//        System.out.println("Details Of Youngest Male Employee In architecture Development");
//        System.out.println("name "+young.getName());
//        System.out.println("salary "+young.getSalary());

//  Que  Who is the oldest employee in the organization?
//  What is his age and which department he belongs to?

        /*Optional <Stream_Empl_Class> oldestEmp = empList.stream().max(Comparator.comparingInt(Stream_Empl_Class::getAge));
        Stream_Empl_Class oldEmployee = oldestEmp.get();
        System.out.println("name "+oldEmployee.getName());
        System.out.println("Age "+oldEmployee.getAge());
        System.out.println("department "+oldEmployee.getDepartment());*/

     /* Map<String,Double> obj= empList.stream().collect(Collectors.toMap(Stream_Empl_Class::getName,Stream_Empl_Class::getSalary));
        System.out.println(obj);*/

//        Set<String> obj = empList.stream().map(Stream_Empl_Class::getName).collect(Collectors.toCollection(HashSet::new));
//        System.out.println(obj);

//    String nameJoin = empList.stream().map(Stream_Empl_Class::getName).collect(Collectors.joining("+"));
//        System.out.println(nameJoin);

       /* Long stucount = empList.stream().count();
        System.out.println("count "+stucount);
        Long stuCount = empList.stream().collect(Collectors.counting());
        System.out.println("stuCount "+stuCount);*/

//        Optional<Double> collectSalary = empList.stream().map(Stream_Empl_Class::getSalary).collect(Collectors.maxBy(Comparator.naturalOrder()));
//        System.out.println("maximum salary "+collectSalary);

//      Map<String,Long> ok =  empList.stream().collect(Collectors.groupingBy(Stream_Empl_Class::getGender,Collectors.counting()));
//        System.out.println(ok);

//    ***  IMPORTANT  TAKE A LOOK ***
    /* Map<String,Integer> refe =empList.stream().collect(Collectors.toMap(Stream_Empl_Class::getName,(Stream_Empl_Class s)->s.getName().length()));
        System.out.println(refe);*/   // name and its length

        Map<String , Integer> empName_Age = empList.stream().collect(Collectors.toMap(Empl_Class_Stream::getName,Empl_Class_Stream::getId));
        System.out.println(empName_Age);



    }
}

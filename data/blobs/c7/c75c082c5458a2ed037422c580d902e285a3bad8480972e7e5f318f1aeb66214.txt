package lab_11_2;

import lab11_1.MyDate;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class Company {
    private String name;
    private ArrayList<Employee> employees = new ArrayList<>();

    public Company(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public void hire(Employee employee){
        if(!employees.contains(employee)){
            employees.add(employee);
        }
    }
    public void hireAll(String csvFile){
        try (Scanner scanner = new Scanner(new File(csvFile))){
            this.employees = new ArrayList<>();
            while (scanner.hasNextLine()){
                String line = scanner.nextLine();
                if (line.isEmpty()) {
                    continue;
                }
                Employee emp = null;
                String[] items = line.split(",");
                if(items.length == 6) {
                    String firstname = items[0].trim();
                    String lastName = items[1].trim();
                    double salary = Double.parseDouble(items[2].trim());
                    int year = Integer.parseInt(items[3].trim());
                    int month = Integer.parseInt(items[4].trim());
                    int day = Integer.parseInt(items[5].trim());
                    emp = new Employee(firstname, lastName, salary, new MyDate(year, month, day));
                }
                else{
                    String firstname = items[0].trim();
                    String lastName = items[1].trim();
                    double salary = Double.parseDouble(items[2].trim());
                    int year = Integer.parseInt(items[3].trim());
                    int month = Integer.parseInt(items[4].trim());
                    int day = Integer.parseInt(items[5].trim());
                    String department = items[6].trim();
                    emp= new Manager(firstname, lastName, salary, new MyDate(year, month, day),department);
                }
                employees.add(emp);
            }
        }
        catch (FileNotFoundException e) {
            System.out.println("File not found: " + csvFile);
            e.printStackTrace();

            }
       }
       public  void fire(int ID){
           for (int i = 0; i < employees.size(); i++) {
               if(employees.get(i).getID() == ID);
               employees.remove(employees.get(i));
           }
       }
       public void printAll(PrintStream ps){
           for (Employee employee : employees) {
               ps.println(employee);
           }
       }
       public void printManagers(PrintStream ps){
           for (Employee employee : employees) {
               if (employee instanceof Manager) {
                   ps.println(employee);
               }
           }
       }
       public void sortByComparator(Comparator<Employee> comp){
           Collections.sort(employees,comp);
       }
    }



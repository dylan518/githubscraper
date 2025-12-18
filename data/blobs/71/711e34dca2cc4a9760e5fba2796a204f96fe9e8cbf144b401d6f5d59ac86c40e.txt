package ObjectsAndClassesLab;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Students_vol2 {

    private static class Student {
        private String firstName;
        private String lastName;
        private int age;
        private String town;

        private Student (String firstName, String lastName, int age, String town){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.town = town;
        }

        public String getFirstName() {
            return this.firstName;
        }

        public void setFirstName(String firstName) {
            this.firstName = firstName;
        }

        public String getLastName() {
            return this.lastName;
        }

        public void setLastName(String lastName) {
            this.lastName = lastName;
        }

        public int getAge() {
            return this.age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        public String getTown() {
            return this.town;
        }

        public void setTown(String town) {
            this.town = town;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        List<Student> listOfStudents = new ArrayList<>();

        while (!input.equals("end")){
            String[] inputArr = input.split(" ");
            String firstName = inputArr[0];
            String lastName = inputArr[1];
            int age = Integer.parseInt(inputArr[2]);
            String town = inputArr[3];

            Student currentStudent = new Student(firstName,lastName,age,town);


            listOfStudents.add(currentStudent);


            input = scanner.nextLine();
        }
        String searchTown = scanner.nextLine();

        for (Student element:listOfStudents) {
            if(element.getTown().equals(searchTown)){
                System.out.printf("%s %s is %d years old%n",element.getFirstName(),element.getLastName(),element.getAge());
            }
        }
    }
}

package ObjectsAndClasses.Lab;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Students {

    static class Student {
        String firstName;
        String lastName;
        String age;
        String town;

        public Student (String firstName, String lastName, String age, String town) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
            this.town = town;
        }

        public String getTown() {
            return this.town;
        }

        public String getFirstName() {
            return this.firstName;
        }

        public String getLastName() {
            return this.lastName;
        }

        public String getAge() {
            return this.age;
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        List<Student> studentList = new ArrayList<>();

        while (!input.equals("end")) {

            String[] inputArr = input.split(" ");

            String firstName = inputArr[0];
            String lastName = inputArr[1];
            String age = inputArr[2];
            String town = inputArr[3];

            Student current = new Student(firstName, lastName, age, town);
            studentList.add(current);

            input = scanner.nextLine();
        }
        String command = scanner.nextLine();

        for (Student student : studentList) {
            String currentTown = student.getTown();
            if (command.equals(currentTown)) {
                String firstName = student.getFirstName();
                String lastName = student.getLastName();
                String age = student.getAge();
                System.out.printf("%s %s is %s years old\n", firstName, lastName, age);
            }
        }
    }
}

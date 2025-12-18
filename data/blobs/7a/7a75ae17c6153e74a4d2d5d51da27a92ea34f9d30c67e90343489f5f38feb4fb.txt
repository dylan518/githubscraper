import java.io.*;
import java.util.ArrayList;
import java.util.List;

import students.Student;


public class Main {

  // написать базу данных студентов
  // студенты могут находиться в группах

  // красиво вывести состав групп на экран
  public static void main(String[] args) throws IOException {
    File studentsFile = new File("res/studentslist.txt");
    List<Student> students = new ArrayList<>();
    // прочитать количество групп
    readGroup(students, studentsFile);
    for (Student student : students) {
      System.out.printf("В группе (%s) %s :%s%n", student.getGroup(), student.getName(),
          student.getEMail());
    }
  }
  // - прочитать название группы
  // - прочитать количество студентов
  // - прочитать информацию о студентах - "имя" или "имя,e-mail" для каждого в отдельной строке
  private static void readGroup(List<Student> students, File studentsFile) throws IOException {
    BufferedReader fileReader = new BufferedReader(new FileReader(studentsFile));
    for (String line = fileReader.readLine(); line != null; line = fileReader.readLine()) {
      String groupName = line.substring(0, line.indexOf(":"));
      Student student = Student.parseStudent(groupName, line);
      students.add(student);
    }
  }
}

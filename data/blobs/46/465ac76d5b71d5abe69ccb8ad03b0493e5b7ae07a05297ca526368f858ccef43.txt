
import java.util.ArrayList;
/**
 * Главный класс нашей программы.
 */
public class Main {
    /**
     * Точка входа в программу.
     * @param args массив строк.
     */
    public static void main(String[] args) {

        WorkingClass workingClass = WorkingClass.getInstance();
        ArrayList<Student> studentArrayList = workingClass.readFromCSVFile();
        workingClass.showStudentArrayList(studentArrayList);

        Student student = new Student(studentArrayList.get(0));
        try {
            Student student1 = (Student) student.clone();
            System.out.println(student1);
            System.out.println(student1.equals(student));
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }


    }
    //Конструктор создан для предотвращения предупреждения при генераций JavaDoc.
    /**
     * Конструктор по умолчанию.
     */
    public Main() {
    }
}
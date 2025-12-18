package itis.hw3.exercise7;

//7) Создайте пример наследования, реализуйте класс Student и класс Aspirant, аспирант отличается от студента
//        наличием некой научной работы. Класс Student содержит переменные: String firstName, lastName, group.
//        А также, double averageMark, содержащую среднюю оценку. Создать метод getScholarship() для класса Student,
//        который возвращает сумму стипендии. Если средняя оценка студента равна 4.7 либо выше, то сумма 3200рублей,
//        если 3.7 - 4.7 2100, иначе не получает ничего.
//        Переопределить этот метод в классе Aspirant.  Если средняя оценка аспиранта равна 4.7 либо выше ,
//        то сумма 5600 рублей, если 3.7 - 4.7 3300, иначе не получает ничего.
//        Создать два списка типа Student, содержащие объекты класса Student и Aspirant.
//        Вызвать метод getScholarship() для каждого элемента списка.

import itis.utils.PrintUtils;

import java.util.ArrayList;
import java.util.List;

import static itis.utils.PrintUtils.println;

public class Exercise7 {

    public static void main(String[] args) {
        Student anton = new Student("Максимов", "Антон", "S-001", 3.2);
        Student maxim = new Student("Аверьянов", "Максим", "S-001", 4.8);
        Student karina = new Student("Исмагилова", "Карина", "S-002", 3.8);
        Student ayaz = new Student("Валиуллин", "Аяз", "S-002", 3.6);
        Student marat = new Student("Валимухаметов", "Марат", "S-003", 3.0);
        List<Student> students = new ArrayList<>(List.of(anton, maxim, karina, ayaz, marat));

        Student elvina = new Aspirant("Фаттахова", "Эльвина", "А-001", 5.0);
        Student marina = new Aspirant("Никитина", "Марина", "А-001", 4.8);
        Student darina = new Aspirant("Кузнецова", "Дарина", "А-002", 3.8);
        Student renat = new Aspirant("Сафин", "Ренат", "А-002", 3.2);
        Student aidar = new Aspirant("Валиев", "Айдар", "А-003", 3.1);
        List<Student> aspirants = new ArrayList<>(List.of(elvina, marina, darina, renat, aidar));

        printAllStudentInfoFromList(students);
        println();
        printAllStudentInfoFromList(aspirants);
    }

    private static void printAllStudentInfoFromList(List<Student> students) {
        students.forEach(PrintUtils::println);
    }
}
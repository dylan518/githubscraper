package home_task_12_10_23.task_3;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        Group group = new Group();

        String firstLetter = "S"; // Задаем первую букву фамилии для поиска
        List<String> foundStudents = group.findStudentsByTheFirstLetter(firstLetter);

        System.out.println("Студенты, чьи фамилии начинаются с буквы '" + firstLetter + "':");
        for (String student: foundStudents){
            System.out.println(student);
        }

    }
}

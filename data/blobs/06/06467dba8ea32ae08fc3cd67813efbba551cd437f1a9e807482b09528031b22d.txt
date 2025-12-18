package _02_JavaFundamentals._17_ExerciseAssociativeArrays;

import java.util.*;

public class _05_Courses {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Map<String, List<String>> coursesMap = new LinkedHashMap<>();

        String input = scanner.nextLine();
        while (!"end".equals(input)) {
            String[] parts = input.split(" : ");
            String courseName = parts[0];
            String registeredStudent = parts[1];

            if (!coursesMap.containsKey(courseName)) {
                coursesMap.put(courseName, new ArrayList<>());
            }

            List<String> students = coursesMap.get(courseName);
            if (!students.contains(registeredStudent)) {
                coursesMap.get(courseName).add(registeredStudent);
            }

            input = scanner.nextLine();
        }

        for (Map.Entry<String, List<String>> entry : coursesMap.entrySet()) {
            System.out.printf("%s: %d%n", entry.getKey(), entry.getValue().size());

            List<String> students = entry.getValue();

            for (String student : students) {

                System.out.printf("--%s%n", student);
            }

        }

    }
}

package javaCore.lesson_17.point_1;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class OOS_Example {

    private static final String FILE_PATH = "src/main/java/org/example/lesson_17/point_1/object";

    public static void main(String[] args) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FILE_PATH))) {
            Person person = new Person("Name", "Surname", 33, new Work("Work"));
            oos.writeObject(person);

            oos.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

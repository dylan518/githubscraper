package com.github.ilebedenko.release_history.java12._3_new_file_method;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * Новый метод Files:
 * <p>
 * `mismatch(Path, Path)` - сравнивает два файла и возвращает индекс первого различающегося байта,
 *                          или -1, если файлы эквивалентны
 */
public class Test {

    public static void main(String[] args) throws IOException {
        Path path1 = Files.createTempFile("test1", ".txt");
        Path path2 = Files.createTempFile("test2", ".txt");

        // equivalent files
        Files.writeString(path1, "Hello!");
        Files.writeString(path2, "Hello!");
        long mismatch = Files.mismatch(path1, path2);
        System.out.println(mismatch);

        // non equivalent files (starting from index 5)
        Files.writeString(path2, "Hello, World!");
        mismatch = Files.mismatch(path1, path2);
        System.out.println(mismatch);
    }
}

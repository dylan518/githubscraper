
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class ReadingFilesPerLine {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // test the method heref
        System.out.print("Enter file name:");
        String fileName = scanner.nextLine();
        read(fileName).stream().forEach(line -> System.out.println(line));
    }

    public static List<String> read(String file) {
        try {
            return Files.lines(Paths.get(file)).collect(Collectors.toList());
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
        return new ArrayList<>();
    }
}
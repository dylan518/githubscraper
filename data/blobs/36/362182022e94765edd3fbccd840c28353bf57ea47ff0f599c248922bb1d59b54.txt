import java.io.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;

public class MyFileWriter {
    public static void main(String[] args) {
        String data = "Hello, World!";
        String fileName2 = "example2.txt";

        printFileSize(".gitignore");

        // 2. Using BufferedWriter

        try (BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(fileName2))) {
            bufferedWriter.write(data);
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        try (BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(".notAPassword.txt"))) {
            bufferedWriter.write("password");
        } catch (IOException e) {
            e.printStackTrace();
        }

        File file = new File(".topSecret");
        file.mkdirs();
        Path filePath = Paths.get(".topSecret", "classified");
        try (BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(filePath.toFile()))) {
            bufferedWriter.write("too bad not telling you any secrets");
        } catch (IOException e) {
            e.printStackTrace();
        }
        printTotalFileSize("example2.txt", ".notAPassword.txt", ".topSecret/classified");
    }

    
    // Calculate and print the file size using the File class
    private static void printFileSize(String fileName) {
        File f = new File (fileName);
        long fSize = f.length();
        System.out.println("file size: " + fSize);
    }

    private static void printTotalFileSize(String... fileNames) {
        long totalSize = 0;
        for (String fileName : fileNames) {
            File file = new File(fileName);
            if (file.exists()) {
                totalSize += file.length();
            }
        }
        System.out.println("Total size of all files: " + totalSize + " bytes");
    }

}
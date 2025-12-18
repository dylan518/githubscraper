import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FileSearch {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        String cmd = in.next();
        if(!cmd.equals("search")) {
            System.err.println("Unknown command: " + cmd + ".");
            in.close();
            return;
        }

        String searchKey = in.next();
        String filePath = in.next();

        in.close();

        try {
            File file = new File(filePath);
            Scanner fileScanner = new Scanner(file);
            List<String> found = new ArrayList<String>();
            for(int lineNbr = 1; fileScanner.hasNextLine(); lineNbr++) {
                String line = fileScanner.nextLine();
                if(line.contains(searchKey)) {
                    found.add(lineNbr + ". " + line);
                }
            }
            if(found.size() > 0) {
                System.out.println("Found " + found.size() + " lines contaning \'" + searchKey + "\' in " + filePath + ":");
                for(String s : found) {
                    System.out.println(s);
                }
            }
            else {
                System.out.println("String \'" + searchKey + "\' not found in " + filePath + ".");
            }
            fileScanner.close();
        } catch(FileNotFoundException e) {
            System.err.println("File \'" + filePath + "\' not found. Please ensure that the file exists and is spelled correctly and try again.");
        }
    }
}

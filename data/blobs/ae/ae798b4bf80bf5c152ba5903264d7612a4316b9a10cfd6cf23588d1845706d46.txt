import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FraseCollector {
    public String collect (int j) throws IOException {
        Scanner scanner = new Scanner(System.in);
        for (int i = 2; i <= j; i=i+2) {
            System.out.println("Enter your next fraze: ");
            String frase = scanner.nextLine();
            FileWriter writer = new FileWriter("src/resources/folder"+i+"/file"+i);
            writer.write(frase);
            writer.flush();
            writer.close();
        }
        scanner.close();
        return "Thank you\n";
    }
}

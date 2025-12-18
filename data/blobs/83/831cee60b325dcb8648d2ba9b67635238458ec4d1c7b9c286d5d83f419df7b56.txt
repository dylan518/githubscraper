import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter the file path of the file you wish to evaluate: ");
            String filePath = scanner.nextLine();
            int max = sumNumbersInFile(filePath);
            System.out.println(max);
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }

    private static int sumNumbersInFile(String filePath) throws FileNotFoundException {
        File file = new File(filePath);
        Scanner scanner = new Scanner(file);

        int sum = 0;

        while (scanner.hasNextInt()) {
            sum += scanner.nextInt();
        }

        return sum;
    }
}
import java.io.IOException;
import java.util.List;
import java.util.Scanner;

public class Calc {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String filename;
        char operation;

        if (args.length != 2) {
            System.out.println("Vous n'avez pas fourni les arguments corrects.");
            System.out.println("Entrez le nom du fichier CSV:");
            filename = scanner.nextLine();
            System.out.println("Entrez l'opération (+ ou *):");
            operation = scanner.nextLine().charAt(0);
        } else {
            filename = args[0];
            operation = args[1].charAt(0);
        }

        InputHandler inputHandler = new InputHandler();
        CalculationLogic calculationLogic = new CalculationLogic();
        OutputHandler outputHandler = new OutputHandler();

        try {
            List<Integer> numbers = inputHandler.readCsv(filename);
            List<String> results = calculationLogic.calculateAndShowResult(numbers, operation);
            outputHandler.displayResults(results);
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}

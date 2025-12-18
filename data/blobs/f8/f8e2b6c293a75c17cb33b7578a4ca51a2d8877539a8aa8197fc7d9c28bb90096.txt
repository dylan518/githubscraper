import java.util.Scanner;

public class TextUI {
    private Scanner scanner;
    private SimpleDictionary diction;

    // Constructors
    public TextUI(Scanner scanner, SimpleDictionary diction) {
        this.scanner = new Scanner(System.in);
        this.diction = diction;  // Use the provided SimpleDictionary instance
    }

    // Methods
    public void start() {
        while (true) {
            System.out.println("Command: ");
            String command, wordAdded, translationAdded, Searchread;
            command = scanner.nextLine();

            if (command.equals("end")) {
                System.out.println("Bye Bye");
                return;
            } else if (command.equals("add")) {
                System.out.println("Word: ");
                wordAdded = scanner.nextLine();
                System.out.println("Translation: ");
                translationAdded = scanner.nextLine();

                this.diction.add(wordAdded, translationAdded);
            } else if (command.equals("search")) {
                System.out.println("To be translated: ");
                Searchread = scanner.nextLine();

                System.out.println(this.diction.translate(Searchread));
            } else {
                System.out.println("Unknown command");
            }
        }
    }
}

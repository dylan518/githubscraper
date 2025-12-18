import java.util.Scanner;
public class while_loop {
    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {
            String name = "";

            while (name.isBlank()) {
                System.out.println("Enter your name: ");
                name = sc.nextLine();
            }
            System.out.println("Hello, " + name + "! How are you?");
            sc.close();
        }
    }
}

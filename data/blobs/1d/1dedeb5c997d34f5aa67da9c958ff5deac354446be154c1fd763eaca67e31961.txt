import java.util.Scanner;

public class PasswordAuthentication {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        try {
            authenticate(password);
            System.out.println("Authentication successful!");
        } catch (AuthenticationFailureException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void authenticate(String password) throws AuthenticationFailureException {
        // Simulated correct password for demonstration purposes
        String correctPassword = "password123";

        if (!password.equals(correctPassword)) {
            throw new AuthenticationFailureException("Authentication Failure: Incorrect password.");
        }
    }
}

class AuthenticationFailureException extends Exception {
    public AuthenticationFailureException(String message) {
        super(message);
    }
}

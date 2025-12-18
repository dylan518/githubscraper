import java.util.Scanner;

public class ObjInputTest {

    public static void main(String[] args) {
        SafeInputObj input = new SafeInputObj(); // Default constructor

        // Test getNonZeroLenString
        String name = input.getNonZeroLenString("Enter your name");

        // Test getRangedInt
        int age = input.getRangedInt("Enter your age", 0, 120);

        // Test getInt
        int luckyNumber = input.getInt("Enter your lucky number");

        // Test getRangedDouble
        double salary = input.getRangedDouble("Enter your desired salary", 30000, 200000);

        // Test getDouble
        double weight = input.getDouble("Enter your weight in kilograms");

        // Test getYNConfirm
        boolean confirm = input.getYNConfirm("Do you want to proceed");

        // Test getRegExString
        String email = input.getRegExString("Enter your email", "^[\\w.%+-]+@[\\w.-]+\\.[a-zA-Z]{2,6}$");

        // Display results
        System.out.println("\nSummary:");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Lucky Number: " + luckyNumber);
        System.out.println("Salary: " + salary);
        System.out.println("Weight: " + weight);
        System.out.println("Proceed: " + (confirm ? "Yes" : "No"));
        System.out.println("Email: " + email);
    }
}
// Given a user's first name, output a welcome message that uses that first name.

// This imports the Scanner class
import java.util.Scanner;

// This creates a class named WelcomeMessage. You can name it whatever you want though.
public class WelcomeMessage {
   // This line sets the starting point for Java.
   public static void main(String [] args) {
      // Initialize Scanner object
      Scanner scnr = new Scanner(System.in);
      // Get username string from user.
      String userName = scnr.next();
      
      // Output the welcome message.
      System.out.println("Hello " + userName + ", and welcome to Java!");
   
   }
}

package myapp.ver1;

import java.io.Console;

public class Hello {
    public static void main(String[] args) {
        // get system console
        Console cons = System.console();
        // Read from the console, the result is assigned to a variable 
        String name = "";
        while (name.trim().length() <= 0) {
            name = cons.readLine("What is your name?");
        }
        // use equals()
        if (name.equals("fred")) {
            System.out.println("Yababadoo");
        } else if (name.equals("barney")) {
            System.out.println("Hello barney");
        } else {
            // Send a greeting to the name 
        System.out.printf("Hello %s.\n\t Nice to meet you\n", name.toUpperCase());
        }
    }
}

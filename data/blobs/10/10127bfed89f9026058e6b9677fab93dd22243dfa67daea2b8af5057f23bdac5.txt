
import java.util.Scanner;

// Define an enum for the days of the week
enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}

public class Days {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the day number (1 to 7):");
        int dayNumber = in.nextInt();

        // Ensure the input is within the valid range
        if(dayNumber < 1 || dayNumber > 7) {
            System.out.println("Invalid day number. Please enter a number between 1 and 7.");
            return;
        }

        // Convert the day number to a Day enum
        Day day = Day.values()[dayNumber - 1]; // Adjusting for zero-based indexing

        Weekdays t = new Weekdays();
        t.nameOfDay(day);
    }
}

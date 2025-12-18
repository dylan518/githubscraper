package Chapter3_Selection.Exercise;

import java.util.Scanner;

public class Soal7MinutesYearsDays {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of minutes: ");
        int minutes = input.nextInt();
        int years = minutes / 525600;
        int days = (minutes % 525600) / 1660;
        System.out.println(minutes + " minutes is approximately " + years + " years and " + days + " days ");
    }
}

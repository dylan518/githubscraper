package app;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter numeral distance which you would like to convert: ");
        double distance = scanner.nextDouble();

        System.out.println("Enter original unit of measurement (miles or kilometers) to convert from:");
        String unit = scanner.next().toLowerCase();

        while (!unit.equals("miles") && !unit.equals("kilometers")) {
            System.out.println("Please enter 'miles' or 'kilometers' for your original (non-converted) distance measurement");
            unit = scanner.next().toLowerCase();
        }

        double convertedDistance;
        if (unit.equals("miles")) {
            convertedDistance = convertMilesToKilometers(distance);
            printConversionResult(distance, "miles", convertedDistance, "kilometers");
        } else {
            convertedDistance = convertKilometersToMiles(distance);
            printConversionResult(distance, "kilometers", convertedDistance, "miles");
        }

        scanner.close();
    }

    private static double convertMilesToKilometers(double miles) {
        return miles * 1.609344;
    }

    private static double convertKilometersToMiles(double kilometers) {
        return kilometers * 0.621371;
    }

    private static void printConversionResult(double originalDistance, String originalUnit, double convertedDistance, String conversionUnit) {
        System.out.println(originalDistance + " " + originalUnit + " = " + convertedDistance + " " + conversionUnit);
    }
}
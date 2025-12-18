import java.util.Scanner;

public class Triangle {
    public static void Trianglechecker(int length, int height) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        System.out.print("Enter '1' to print the perimeter of the triangle, or '2' to print the shape of the triangle: ");
        //checks if the entered input is correct
        while (true) {
            try {
                choice = scanner.nextInt();
                if (choice < 1 || choice > 2) {
                    System.out.println("Invalid input. Please enter a number between 1 and 2.");
                    continue;

                }
                break;
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a number between 1 and 2.");
                scanner.nextLine();

            }
        }
        if (choice == 1) {
            trianglePerimeterPRINTER(length,height);
        }
        else {
            printTriangle(length, height);

        }
    }


    private static void trianglePerimeterPRINTER(int length,int height) {
        // Calculate the length of the equal sides
        double side = Math.sqrt(Math.pow(length/2, 2) + Math.pow(height, 2));

        // Calculate the perimeter
        double perimeter = 2 * side + length;
        System.out.println("Perimeter of triangle is: " + perimeter);
    }


    // prints the shape of the triangle from asterisks.
    public static void printTriangle(int length, int height) {
        if (length % 2 == 0 || length > height * 2) {
            System.out.println("The triangle cannot be printed.");
        } else {
            int divisor=countOddDivisors(length);//how many odd numbers go into length excluding 1 and itself.
            int NumofRows=(height-2)/divisor;// How many times of each row type
            int remainder = (height-2) % divisor;
            printline(1,length);
            for (int i = 0; i < remainder; i += 1) {//print lines of three asterisks as the number of the remainder
                printline(3,length);
            }
            int numstars=3;
            for (int i = 0; i <divisor ; i += 1) {
                for (int J = 0; J < NumofRows; J += 1) {
                    printline(numstars, length);

                }
                numstars+=2;
            }
            printline(length, length);
            System.out.println();

        }
    }

    public static int countOddDivisors(int num) {
        int count = 0;
        for (int i = 2; i < num; i++) {
            if (i % 2 != 0) {
                count++;
            }
        }
        return count;
    }
    //prints a line of asterisks
    public static void printline (int star, int length) {
        int space=(length-star)/2;
        for (int i = 0; i < space; i += 1) {
            System.out.print(" ");
        }
        for (int i = 0; i < star; i += 1) {
            System.out.print("*");
        }
        for (int i = 0; i < space; i += 1) {
            System.out.print(" ");
        }
        System.out.println();

    }

}

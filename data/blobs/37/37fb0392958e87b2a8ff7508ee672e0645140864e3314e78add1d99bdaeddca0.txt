package W1.Extra2;

import java.util.HashSet;
import java.util.Scanner;

public class Ex8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HashSet<Integer> set = new HashSet<Integer>();
        System.out.print("Enter 10 numbers: ");

        for (int i = 0; i < 10; i++) {
            set.add(scanner.nextInt());
        }

        System.out.println("The number of distinct number is: " + set.size());

        System.out.print("The distinct integers are: ");
        for (int i : set) {
            System.out.print(i + " ");
        }

    }
}

package anagram;

import java.util.Scanner;

public class InputCLI {
    private static final Scanner scanner = new Scanner(System.in);

    public static Function functionInput() {
        System.out.print("Welcome to Anagram checker. Please, select a function you want to execute:\n" +
                "1. Check if two strings are anagrams\n" +
                "2. Show all found anagrams for a string\n" +
                "3. Close program\n");

        String function = scanner.nextLine();
        switch (function) {
            case "1":
                return Function.ANAGRAM_CHECKER;
            case "2":
                return Function.ANAGRAM_LIST;

            case "3":
                return Function.CLOSE;

            default:
                System.out.println("The input is not correct.");
                return functionInput();

        }
    }

    public static AnagramInput anagramCheckInput() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Please enter first text: \n");
        String first = scanner.nextLine();
        System.out.println("Please enter second text: \n");
        String second = scanner.nextLine();
        return new AnagramInput(first, second);

    }

    public static String anagramListInput() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Please enter string to get anagrams for.\n");
        return scanner.nextLine();

    }
}

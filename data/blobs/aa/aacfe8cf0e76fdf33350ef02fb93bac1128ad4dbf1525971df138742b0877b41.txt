public class CommandLineExample {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please provide an integer as a command line argument.");
            return;
        }

        String numberString = args[0];
        int number = convertStringToInt(numberString);
        System.out.println("Converted integer: " + number);
    }

    public static int convertStringToInt(String numberString) {
        int result = 0;
        boolean isNegative = false;

        // Check if the number is negative
        if (numberString.charAt(0) == '-') {
            isNegative = true;
            numberString = numberString.substring(1); // Remove the negative sign
        }

        // Convert each character to an integer and compute the result
        for (int i = 0; i < numberString.length(); i++) {
            char c = numberString.charAt(i);
            if (c < '0' || c > '9') {
                System.err.println("Invalid input. Please provide a valid integer string.");
                System.exit(1); // Exit the program with an error status
            }
            int digit = c - '0'; // Convert character to integer
            result = result * 10 + digit;
        }

        // If the number is negative, make the result negative
        if (isNegative) {
            result = -result;
        }

        return result;
    }
}

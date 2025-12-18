public class CommandLineString {
    public static void main(String[] args) {
        String inputString = args[0];

        int length = inputString.length();
        System.out.println("Length of the string: " + length);

        System.out.println("Content of string character by character:");
        for (int i = 0; i < length; i++) {
            System.out.print(inputString.charAt(i) + " ");
        }
        System.out.println();

        StringBuilder convertedString = new StringBuilder();
        for (int i = 0; i < length; i++) {
            char c = inputString.charAt(i);
            if (Character.isUpperCase(c)) {
                convertedString.append(Character.toLowerCase(c));
            } else if (Character.isLowerCase(c)) {
                convertedString.append(Character.toUpperCase(c));
            } else {
                convertedString.append(c);
            }
        }
        System.out.println("Converted string: " + convertedString.toString());
    }
}
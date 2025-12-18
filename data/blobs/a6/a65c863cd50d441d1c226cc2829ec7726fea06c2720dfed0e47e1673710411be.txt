//Assume that there is a cryptographic algorithm which takes an input text ‘A’
// composed of lower and upper case characters. Separately a character string ‘B’ is
// defined. Each character from B has an associated random integer value between 1 and 100.
// The algorithm checks if the letters from B are found in A and adds
// the associated numerical values. To the final sum value, the algorithm also adds the
// positions from string A where characters
//from string B were found. If the final sum is larger than 100, the encryption was valid.
// Display a message with the result.
//Example:
//String A = ”aTmPpDsst”
//String B =”ams”
//Associated numerical values for string B: 11 33 7
//Sum: (11+33+7+7)+(1+3+7+8)=77 -> INVALID ENCRYPTION

import java.util.Random;
import java.util.Scanner;

public class HorvathDaiana_lab3pb10 {
    public static void checkString(String string1, String string2) {
        StringBuilder result = new StringBuilder();
        int count;
        for (int i = 0; i < string1.length(); i++) {
            char c = string1.charAt(i);
            if (string2.indexOf(c) != -1) {
                result.append(c);
            }

        }
        if (result.isEmpty())
        {
        System.out.println("There are no common characters found!");
        System.exit(1);
        }
        else {
            System.out.println("Characters found: " + result);
        }

    }
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);

        System.out.println("Enter a string containing both uppercase and lowercase letters: ");
        String A=scanner.next();
        String B="aHojM";
        boolean hasUppercase=A.matches(".*[A-Z].*");
        if (!hasUppercase) {
            System.out.println("Enter bot uppercase and lowercase characters!");
            System.exit(1);
        }
        Random random=new Random();
        int upperlimit=100;
        int lowerimit =1;
        checkString(B,A);
        for (int i=0; i<B.length(); i++)
        {
            char c= B.charAt(i);
            System.out.println("The character "+c+" has the number: " +random.nextInt(lowerimit, upperlimit) );

        }





    }
}
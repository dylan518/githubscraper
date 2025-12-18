package unit02.lesson28;
/*
    In computers the * character is often used to represent wildcard characters that may be
substituted for any set of characters. For instance, if you search a file directory for *.txt
your computer returns a list of all files in the directory with the .txt extension.
For this assignment you will input a String that contains a single * character, then a second
String. The * will be replaced by the second String. So for example, if the user enters the
Strings "d*g" and "in", the program outputs ding.
The original String must contain only letters of the alphabet, capital or lowercase, spaces
and tab, and a single *. The replacement String may be any legal String in Java.
If the first String does not contain a * “Error: no *“ should be output.
If the first String contains anything other than letters of the alphabet, spaces or tabs then
“Error: Incorrect characters“ should be printed. If the first String does not have a * you do
not have to check for incorrect characters, only “Error: no *“ should be output.
Sample Run 1:
Enter the first String:
D*g
Enter the replacement String:
in
Ding

Sample Run 2
Enter the first String:
$Wild*$
Enter the replacement String:
Card
Error: Incorrect characters
     */

import java.util.Scanner;

public class Wildcard {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the first string: ");
        String string1 = scanner.next();
        System.out.println("Enter replacement String: ");
        String replacementString = scanner.next();
        boolean star = false;
        for (char letter : string1.toCharArray()) {
            if (letter == '*') {
                if (!star) {
                    star = true;
                } else {
                    System.out.println("Incorrect characters");
                    return;
                }
            } else if (!((letter >= 'A' && letter <= 'Z') || (letter >= 'a' && letter <= 'z'))){
                System.out.println("Incorrect characters");
                return;
            }
        }
        if (!star){
            System.out.println("Incorrect characters");
            return;
        }
        int starLocation = string1.indexOf('*');


        String beginning = string1.substring(0, starLocation);
        String ending = string1.substring(starLocation + 1);
        System.out.println(beginning + replacementString + ending);
    }
}


import java.util.Scanner;
public class Assignment1C
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("[And the next letter is]");
        System.out.println("Please enter a letter: ");
        char letter = scan.next().charAt(0);
        char letter2 = (char) (letter+1);
        char letter3 = (char) (letter+2);
        char letter4 = (char) (letter+3);
        char letter5 = (char) (letter+4);
        System.out.println("The next letters after" + " " + letter + " " + "are" + " " + letter2 + "," + " " + letter3 + "," + " "+ "and" + " " + letter4 + "!");



    }
}

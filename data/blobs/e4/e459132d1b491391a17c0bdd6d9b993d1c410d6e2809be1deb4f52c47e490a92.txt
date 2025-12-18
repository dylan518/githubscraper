import java.util.Scanner;
public class LeftShift {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a: ");
        int a = sc.nextInt();
        int b = a << 2;
        System.out.println("LeftShift of a is: " +b);
    }
}
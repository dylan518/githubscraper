
import java.util.Scanner;
public class Lab7C{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        System.out.println("Please enter a value for the size: ");
        int size = scan.nextInt();

        System.out.println("This is the requested " + size + "x" + size + " right-triangle:");
        for(int a=1; a<=size;a++){
            for(int b=size-a; b>0;b--){
                System.out.print(" ");
            }
            for(int c = size - a + 1; c <= size; c++){
                System.out.print("*");
            }
            System.out.println();
        }

    }
}

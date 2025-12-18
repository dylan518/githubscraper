package Kattis;
import java.util.Scanner;
public class EnterWords {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        int z = input.nextInt(), y = input.nextInt();
        String str;

        for(int x = 0; x<z; x++){
            str = input.next();
        }
        System.out.print(y);
    }
}

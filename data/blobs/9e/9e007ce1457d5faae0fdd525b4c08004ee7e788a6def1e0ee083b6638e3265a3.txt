package BasicDS.Question1;

import java.util.Scanner;
//import BasicDS.Question1.CheckArmstrong;

public class Question1 {
    public static void main(String[] args) {
        Scanner scanner =new Scanner(System.in);
        int n = scanner.nextInt();
        if(CheckArmstrong.isArmstrong(n)){
            System.out.println("It is an armstrong number");
        }
        else {
            System.out.println("It is not an armstrong number");
        }
    }
}

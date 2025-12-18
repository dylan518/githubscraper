package ca.ciccc.wmad.assignment3.question10;

import java.util.Scanner;

public class Question10 {

    public static void invoke(){
        String function1 = functionCreator();
        String function2 = functionCreator();
        System.out.println("function 1 created : "+ function1);
        System.out.println("function 2 created : "+ function2);
        System.out.println(checkSingleFactorEquality(function1,function2));

    }
    public static String functionCreator() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a coefficient number: ");
        int coefficient= input.nextInt();

        System.out.println("Enter a baseFactor letter: ");
        String baseFactor= input.next();

        System.out.println("Enter a exponent number: ");
        int exponent = input.nextInt();

        return (coefficient + "*" + baseFactor + "^" + exponent);
    }
    public static boolean checkSingleFactorEquality(String function1,String function2){
        if (function1.equalsIgnoreCase(function2)){
            return true;
        }
        else {
            return false;
        }
    }
}

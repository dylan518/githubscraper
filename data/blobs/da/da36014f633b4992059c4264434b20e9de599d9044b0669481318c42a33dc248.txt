package upcast;

import java.util.Scanner;

public class PrintEvenNumberText {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the input text :");
//        String inputtext=s.nextLine();
//        teString inputtext= "hello bhai kaise ho";
        String[] text= s.nextLine().split(" ");
        int count=0;
        for(String outputtext:text){
            if(outputtext.length()%2==0) {
                count++;
                System.out.println(outputtext + " text with a length of " + outputtext.length());
//                System.out.println(outputtext.length());
            }
        }
        System.out.println("number of even number text occurrences: "+ count);
//        System.out.println(inputtext);
    }
}

package decision_structures;

import java.util.Scanner;

public class Feb09RelationalOperators {
    public static void main(String[] args){
        //6 Relational operators: > < >= <= == !=
        //Logical operators: && || !

        Scanner scanner = new Scanner(System.in);


        boolean qualifyLoan;
        int idealSalary = 30000;
        int minimumWorkingYears = 2;

        String personsName = "Roberto";

        System.out.println("Enter your salary:");
        int personSalary = scanner.nextInt();
        System.out.println("Enter the years you've been working at your current job:");
        int personWorkingYears = scanner.nextInt();

        if(personSalary >= idealSalary && personWorkingYears >= minimumWorkingYears){
            System.out.println("Congrats " + personsName + ". You qualify for a loan");
        }else{
            System.out.println("Sorry, you don't qualify for a loan");
        }

        scanner.close();

    }//main


}//class Feb09RelationalOperators

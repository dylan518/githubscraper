package Class4;

import java.util.Scanner;

public class H1Loan {
    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);

        System.out.println("Please Enter Amount of Loan You Want");
        double amountLoanValue=scanner.nextDouble();
        if(amountLoanValue<=200000)
        {
            System.out.println("we are able to give you money");
        }
        else {
            System.out.println("We will reject you ");
        }

    }
}

/*  JavaPaycheck
    Ben Simpson
    CIS084 Java Programming
    Inputs: hours, payRate
    Output: grossPay, taxes, netPay
 */
package paycheck;
import java.util.Scanner; // Used to read from the keyboard

public class Paycheck {

    // define the constants
    public static final double OVERTIME_RATE = 1.5; //time and a half
    public static final double TAX_RATE = 0.17; //0.17 is 17%

    public static void main(String[] args) {
        //declare the variables
        double hours, payRate;
        double regHours, overtimeHours;
        double regPay, overtimePay;
        double grossPay, taxes, netPay;

        // create the stdin object (to use the keyboard)
        Scanner stdin = new Scanner(System.in);

        // INPUT: hours and payRate
        System.out.print ("Enter the hours worked: "); //prompt message
        hours = stdin.nextDouble();
        System.out.print ("Enter the pay rate: ");
        payRate = stdin.nextDouble();

        // Process: compute the paycheck
        //  separate the regular and overtime hours
        //  compute regular, overtime and total paycheck
        if (hours <= 40.0)  // less or equal to 40. No overtime
        {
            regHours = hours; // separate regHours and overtimeHours
            overtimeHours = 0.0;
        }
        else    // over 40. How much is overtime?
        {
            regHours = 40.0;    // regular pay for the first 40 hours
            overtimeHours = hours - 40.0;   // anything over 40 hours
        }
        regPay = regHours * payRate;
        overtimePay = overtimeHours * payRate * OVERTIME_RATE;
        grossPay = regPay + overtimePay;
        taxes = grossPay * TAX_RATE;
        netPay = grossPay - taxes;

        // output: display the paycheck values with to digits past the decimal
        System.out.printf ("\n"); // new line before output
        System.out.printf ("Your gross pay is $%.2f\n", grossPay);
        System.out.printf ("Your taxes are $%.2f\n", taxes);
        System.out.printf ("Your net pay is $%.2f\n", netPay);

        // Close stdin - it is no longer needed in the program
        stdin.close()
    } // end of public static void main(Sting[] args)
} // end of public class Paycheck
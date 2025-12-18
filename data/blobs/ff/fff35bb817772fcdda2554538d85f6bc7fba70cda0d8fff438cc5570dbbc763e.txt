import java.util.Scanner;

public class conditon_1 {

    public static void main(String[] args) {
        //System.out.println("Enter the age for driving:");
       // Scanner age = new Scanner(System.in);
       // int y = age.nextInt();
       int age =19;
        boolean cond=(age==18);

        // Decision making function in java:
        // 1.If-else(Condition) statement
        // 2.switch() statement
        // '='>>>>it means to assign value to variable
        // '=='>>>> it means to check condition which is true or false

        if (cond) {
            // here when y become 18 then it gives true while it will be false
            System.out.println("Yes you can drive!");
        }
        // else is an optional ......
        else {
            System.out.println("Not you cannot drive yet!");
        }

        // relational operator
        // ==>>>equal to , >=....greater than equal to ,,, <=...less than equal
        // to,,,,,!=....not equal to ,,,,>....greater than,,,,,and <...less than
    }
}
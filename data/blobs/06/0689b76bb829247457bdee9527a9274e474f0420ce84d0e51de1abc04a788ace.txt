import java.util.Scanner;

public class assignment1_244107060062 {
    public static void main(String[] args) {
        Scanner input244107060062 = new Scanner(System.in);

        int num1, num2, num3, max;

        System.out.print("Input the num1: ");
        num1 = input244107060062.nextInt();
        System.out.print("Input the num2: ");
        num2 = input244107060062.nextInt();
        System.out.print("Input the num3: ");
        num3 = input244107060062.nextInt();

        if(num1>num2)
            if(num1>num3)
                max = num1;
            else
                max = num3;
        else
            if(num2>num3)
                max = num2;
            else
                max = num3;

        System.out.print("Max number: " + max);
    }
}


package JD07;

import java.util.Scanner;

public class MilesToKM {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        System.out.print("Enter the miles: ");
        double miles=input.nextDouble();
        double km=miles*1.60934;
        System.out.println(miles+" miles is equal to "+km+" kilometers ");
        input.close();
    }
}

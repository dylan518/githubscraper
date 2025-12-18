import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        System.out.println("Wage calculator");

        System.out.print("Enter employee's wage value: ");
        double wage = read.nextDouble();

        if(wage <= 280.00){
            double percent = 0.2;
            double valueAdjust = wage * percent;
            double readjustment = wage + (wage * percent);
            System.out.println("Wage before readjustment: " + wage + " |With adjustment of 20%: " + valueAdjust + "|With readjust: " + readjustment);
        }else if (wage > 280.00 && wage <= 700.00) {
            double percent = 0.15;
            double valueAdjust = wage * percent;
            double readjustment = wage + (wage * percent);
            System.out.println("Wage before readjustment: " + wage + " |With adjustment of 15%: " + valueAdjust + "|With readjust: " + readjustment);
        }else if (wage > 700.00 && wage <= 1500.00) {
            double percent = 0.1;
            double valueAdjust = wage * percent;
            double readjustment = wage + (wage * percent);
            System.out.println("Wage before readjustment: " + wage + " |With adjustment of 10%: " + valueAdjust + "|With readjust: " + readjustment);
        }else {
            double percent = 0.05;
            double valueAdjust = wage * percent;
            double readjustment = wage + (wage * percent);
            System.out.println("Wage before readjustment: " + wage + " |With adjustment of 5%: " + valueAdjust + "|With readjust: " + readjustment);
        }
    }
}
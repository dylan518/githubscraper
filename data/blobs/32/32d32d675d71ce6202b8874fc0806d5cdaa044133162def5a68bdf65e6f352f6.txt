import java.util.Scanner;

public class Nnum_sum {
    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);

        int count=1;
        int sum=0;



        System.out.println("Enter the amount of numbers "+count);
        int amount= input.nextInt();

        while (count<=amount){
            System.out.println("Enter the numbers  "+count);
            int numbers=input.nextInt();

            sum=sum+numbers;


            count++;
        }
        System.out.println("Sum of numbers = "+sum);


    }
}

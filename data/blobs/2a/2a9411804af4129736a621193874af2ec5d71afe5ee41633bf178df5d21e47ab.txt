import java.util.*;

public class Question1e {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num, b, c, sum1 = 0, sum2 = 0, diff;
        System.out.println("enter a number");
        num = sc.nextInt();

        b = num;
        while (b != 0) {
            c = b % 10;
            if (c % 2 == 0 && c % 4 != 0) {
                sum1 += c;
            } else if (c % 2 != 0 && c % 3 != 0) {
                sum2 += c;
            }
            b /= 10;
        }
        diff = sum1 - sum2;
        System.out.println("diff = " + diff);
        sc.close();
    }

}

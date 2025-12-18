package ss5_loop;

import java.util.Scanner;

//Tính tổng và tích các chữ số của một số m, m được nhập từ bàn phím
//(Ví dụ : m = 234 => S = 2 + 3 + 4 = 9, P = 2 * 3 * 4 = 24)

public class Ex12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Hay nhap m: ");
        int m = scanner.nextInt();
        int s = 0;
        int p = 1;
        int digit;

        while (m > 0) {
            digit = m % 10; //4
            s = s + digit;
            p = p * digit;
            m = m / 10; //23
        }
        System.out.println("Tong la: " + s);
        System.out.println("Tich la: " + p);
    }
}

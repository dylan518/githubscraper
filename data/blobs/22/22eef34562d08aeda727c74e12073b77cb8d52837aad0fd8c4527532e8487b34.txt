package n2753;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Title : 윤년
 * Link : https://www.acmicpc.net/problem/2753
 */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            int year = scanner.nextInt();

            if (!(1 <= year && year <= 4000))
                throw new RuntimeException("연도는 1부터 4000까지 입력가능 합니다.");

            System.out.println(year % 4 == 0 && (year % 100 != 0 || year % 400 == 0) ? "1" : "0");
        } catch (InputMismatchException e) {
            System.out.println("숫자가 아닙니다.");
        } catch (RuntimeException e) {
            System.out.println(e.getMessage());
        }
    }
}

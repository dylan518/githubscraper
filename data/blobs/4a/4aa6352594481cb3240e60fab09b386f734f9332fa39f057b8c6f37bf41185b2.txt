package Level_5;

import java.util.Scanner;

public class No1065 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print(arithmetic_sequence(sc.nextInt()));
        sc.close();
    }
    public static int arithmetic_sequence(int num) {
        int count = 0; //한수 카운트
        if (num < 100) return num;
        else {
            count = 99;

            for (int i = 100; i <= num; i++) {
                int hun = i / 100; //백의 자리
                int ten = (i / 10) % 10; //십의 자리
                int one = i % 10; //일의 자리

                if ((hun - ten) == (ten - one)) count++; //각 자리수가 수열을 이룰 때
            }
        }
        return count;
    }
}
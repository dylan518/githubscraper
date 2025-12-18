package 문자열1.형성평가04;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.next();
        String str2 = sc.next();

        char[] c = new char[100];


        for (int i = 0; i < str.length(); i++) {
            c[i] = str.charAt(i);
            if (c[i] == str2.charAt(0)) {
                System.out.print(i);
                break;
            } else if (i == str.length() - 1)
                System.out.println("No");
        }
    }
}
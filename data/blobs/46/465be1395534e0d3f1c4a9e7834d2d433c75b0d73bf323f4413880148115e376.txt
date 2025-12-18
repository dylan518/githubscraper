package scanner;

import java.util.Scanner; //자바 라이브러리

public class Scanner1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); //스캐너 만듦.

        System.out.print("문자열을 입력하세요.");
        String str = scanner.nextLine(); //입력을 String으로 가져온다. / 엔터를 입력할때까지 문자를 가져온다.
        System.out.println("입력한 문자열 = " + str);

        System.out.print("정수를 입력하세요:");
        int inValue = scanner.nextInt(); //입력 int형으로 가져온다. 정수 입력에 사용한다.
        System.out.println("입력한 정수 = " + inValue);

        System.out.print("실수를 입력하세요:");
        double doubleValue = scanner.nextDouble(); // 입력을 double형으로 가져온다. 실수 입력에 사용한다.
        System.out.println("입력한 실수:" + doubleValue);
    }
}


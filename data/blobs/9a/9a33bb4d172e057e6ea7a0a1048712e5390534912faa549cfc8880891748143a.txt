package 함수형프로그래밍예제2번;

import java.util.function.IntBinaryOperator;

// 메소드 참조 : 메소드 참조해서 매개변수의 정보 및 반환 타입을 알아 내어, 불 필요한 매개변수를 제거 함

class Calculator {
    public static int staticMethod(int x, int y) {
        return x + y;
    }
    public int instanceMethod(int x, int y) {
        return x + y;
    }
}
public class FunctionEx2 {
    public static void main(String[] args) {
        IntBinaryOperator operator; // 두 개의 int 연산하는 인터페이스
        // 정적 메소드 참조 (static이 아니면 바로 참조할 수는 없음.)
        operator = (x,y) -> Calculator.staticMethod(x,y);
        System.out.println("결과 1 : " + operator.applyAsInt(1,2)); // 두 개의 int 연산
        // 메소드 참조 방식  클래스::메소드
        operator = Calculator::staticMethod;  // :: 으로 참조하여 매개변수를 생략했다.
        System.out.println("결과 2 : " + operator.applyAsInt(1,2));

        // 인스턴스 메소드 참조 (static이 아닌 메소드이므로 new로 객체를 생성한 후)
        Calculator obj = new Calculator();
        operator = (x,y) -> obj.instanceMethod(x, y);
        System.out.println("결과 3 : " + operator.applyAsInt(5,6));

        // static이 아니니까 obj객체로 고정 후
        operator = obj::instanceMethod;
        System.out.println("결과 4 : " + operator.applyAsInt(7,8));

    }
}

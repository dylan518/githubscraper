package c15_casting.animals;
/*
    c15_casting 패키지 생성
    animals 패키지 생성
    Main
    Animal
    Dog

    참조 자료형 캐스팅(Reference Type Casting)
        객체 지향 프로그래밍(OOP)에서 중요한 요소 중 하나입니다.

        1. 참조 자료형이란?
            자바에서의 자료형은 크게 두 가지로 구분됨.
                1) 기본 자료형(Primitive Types) : int, double, char등
                2) 참조 자료형(Reference Types) : 객체를 참조하는 변수로 클래스나 인터페이스를 통해 생성된 객체

            참조 자료형 캐스팅 : 객체의 자료형을 변환하는 작업
                캐스팅 종류
                    1) 업캐스팅 : 하위 클래스의 객체를 상위 클래스 타입으로 변환
                    2) 다운캐스팅 : 상위 클래스 타입의 객체를 하위 클래스 타입으로 변환

                알아야 할 사항 : 연산자(Operator) instanceof -> 연산자 개념은 첫주차에 학습했습니다.
                    ex) 1 + 1 = 2에서 +가 연산자에 해당

        2. 업캐스팅 - 암시적(implicit)으로 이루어짐 -> 저희는 자동으로 바뀐다고 생각하시면 됩니다.
        3. 다운캐스팅 - 명시적(explicit)으로 이루어짐 -> 반드시 개발자가 직접 바꿔줘야 한다고 생각해야 함.

        4. 업캐스팅과 다운 캐스팅의 활용
            캐스팅은 주로 다형석(Polymorphism)을 구현할 때 사용함. 상위 클래스 타입으로 객체를 처리하면서도
            특정 상황에서는 하위 클래스의 고유 기능을 사용할 수 있음

        5. 캐스팅의 장단점
            장점 :
                코드 유연성 : 업태스팅을 통해 '다양한 객체를 하나의 상위 클래스 타입으로 관리' 가능
                다형성 구현 : 메서드 오버라이딩과 함께 사용하면 코드 재사용성을 높일 수 있음.

            단점 :
                다운 캐스팅의 위험성 : 잘못 다운 캐스팅을 하게 됩니다.
                    예를 들어 상위 클래스 A와 하위 클래스 B, C가 있다고 가정했을 때, B의 객체인 b를 A로
                    업캐스팅한 후, C로 다운 캐스팅하는 문제가 생길 수 있어 주의가 필요함.

                복잡성 증가 : 코드 가독성이 떨어질 수 있음 -> 이렇게 바꿨다가 저렇게 바꿨다가 하기 때문인데
                    특히 업캐스팅의 경우 암시적으로 일어나기 때문에 어디서 바뀌었는지 확인은 못하고 있다가
                    갑자기 다운캐스팅이 튀어나오는 경우에 초심자들이 코드를 읽는게 힘겨울 수 있습니다.

    instance of 연산자 : Java에서 객체의 실제 타입을 검사하는 데 사용(어떤 클래스의 객체인지를 확인하는 용도)
        -> 주로 다운 캐스팅의 안전성을 확보하기 위해서 사용함.

        형식 :
            object(객체명) instanceof ClassName(클래스명) -> 1 + 1 생각하라고 수업했습니다.

            object : 검사하려는 객체명
            ClassName : 객체가 검사될 클래스나 인터페이스

            반환값은 object가 ClassName의 인스턴스이거나 ClassName의 하위 클래스의 인스턴스인 경우 true 반환,
            아니면 false를 반환함.
 */
public class Main {
    public static void main(String[] args) {
        // Dog 객체 생성
        Dog dog1 = new Dog();

        // 메서드를 활용
        // 오버라이딩한 메서드
        dog1.makeSound();
        // Dog 클래스의 자체 메서드
        dog1.fetch();

        // Animal 객체 생성
        Animal animal1 = dog1;  // 업캐스팅 1번 방법
        animal1.makeSound();    // 'Dog'의 makeSound() 메서드가 실행됨
//      animal1.fetch();      // 타입이 Animal로 선언돼있기 때문에
                                // Animal 클래스에는 없는 fetch() 메서드를
                                // 호출할 수 없음

        System.out.println("------animal2 부분 시자깁니다------");
        Animal animal2 = new Dog();     // 업캐스팅 2번 방법 -> 얘가 정처기 등 자격증 시험에 더 자주 나옵니다.
        // A a = new B();
        animal2.makeSound();        // 'Dog'의 재정이된 makeSound()가 호출됨.
//      animal2.fetch();            // animal1때와 동일하게 호출 불가능함.

        Animal animal3 = new Animal();
        boolean result1 = (animal1 instanceof Animal);
        boolean result2 = (animal1 instanceof Dog);
        System.out.println(result1);
        System.out.println(result2);

        System.out.println("animal2 검증입니다.");
        boolean result3 = (animal2 instanceof Animal);
        boolean result4 = (animal2 instanceof Dog);
        System.out.println(result3);
        System.out.println(result4);

        System.out.println("animal3 검증입니다.");
        boolean result5 = (animal3 instanceof Animal);
        boolean result6 = (animal3 instanceof Dog);
        System.out.println(result5);
        System.out.println(result6);

        // 다운 캐스팅 관련 수업
        Dog dog2 = (Dog) animal2;   // 다운캐스팅의 경우 명시적으로 쓰여야하기 때문에
                                    // 이전에 배운 형변환 방식인 '(클래스명)'을 사용해야 합니다.
                                    // 이전까지는 double pi = 3.14;
                                    // int three = (int) pi; 와 같은 방식으로 작성했지만
                                    // 이제는 클래스와 객체 단위에서 생각할 필요가 있습니다.
        dog2.makeSound();           // 이제는 대놓고 Dog 클래스의 객체이기 때문에 재정의된 makeSound()호출
        dog2.fetch();               // 이제는 Dog 클래스의 객체이기 때문에 fetch() 메서드 호출 가능.

//        Dog dog3 = (Dog) animal3;
//        dog3.makeSound();
//        dog3.fetch();
        /*
            이상의 코드를 실행하려고 하면
            Execution failed for task ':c15_casting.animals.Main.main()'.
            > Process 'command 'C:\Users\alswp\.jdks\corretto-17.0.13\bin\java.exe'' finished with non-zero exit value 1

            * Try:
            > Run with --stacktrace option to get the stack trace.
            > Run with --info or --debug option to get more log output.
            > Run with --scan to get full insights.
            > Get more help at https://help.gradle.org.
            BUILD FAILED in 363ms
            2 actionable tasks: 2 executed
            컴파일 오류가 발생합니다.

            그 이유는 :
                애초에 Animal로 만든 것을 아무런 번형 없이 강제적으로 다운캐스팅을 시도했기 때문입니다.

            이상과 같은 컴파일링 오류를 막기 위한 방식으로 코드를 아래와 같이 작성할 수 있습니다.
         */

        Animal animal4 = new Dog();

        // 컴파일링 오류를 막기 위한 다운 캐스팅 방법
        System.out.println("animal4 검증 부분입니다.");
        if (animal4 instanceof Dog){
            Dog dog4 = (Dog) animal4;   // 위에 조건문이 true일때만 현재 코드라인이 실행되기 때문에
                                        // 컴파일링 오류가 발생하지 않음.
            dog4.makeSound();
            dog4.fetch();
        }


    }
}

package ch09nested.book.sec04.exam03;

public class A {
    public void method1(int arg) {  // final int arg
        int var = 1;                // final int var

        // 로컬 클래스
        class B {
            void method2() {
                System.out.println("arg : " + arg);
                System.out.println("var : " + var);

//                arg = 2; //  로컬클래스에서 사용하게 되면 final 특성을 갖기때문에
//                var = 2; //  로컬클래스에서 사용하게 되면 final 특성을 갖기때문에
            }
        }

        B b = new B();
        b.method2();


    }
}

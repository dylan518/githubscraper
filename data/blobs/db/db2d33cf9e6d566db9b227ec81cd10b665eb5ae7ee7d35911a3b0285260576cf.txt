package chapter03.polymorphism01;

public class Driver {
    public static void main(String[] args) {
        Penguin pororo = new Penguin();

        pororo.name = "뽀로로";
        pororo.habitat = "남극";

        // 오버라이딩 메서드 실행
        //      Animal 객체의 showName() 메서드는 오버라이딩된 Penguin 객체의 showName() 메서드에 의해 가려짐
        pororo.showName();
        pororo.showName("초보람보");  // 오버로딩 메서드 실행
        pororo.showHabitat();

        // Penguin 인스턴스 생성
        //      Animal 인스턴스도 함께 생성되어 힙 영역에 배치됨
        Animal pingu = new Penguin();
        pingu.name = "핑구";

        // 오버라이딩 메서드 실행
        //      Animal 객체의 showName() 메서드는 오버라이딩된 Penguin 객체의 showName() 메서드에 의해 가려짐
        // 상위 클래스 타입의 객체참조변수를 사용하더라도 하위 클래스에서 오버라이딩한 메서드가 호출됨
        pingu.showName();
    }
}

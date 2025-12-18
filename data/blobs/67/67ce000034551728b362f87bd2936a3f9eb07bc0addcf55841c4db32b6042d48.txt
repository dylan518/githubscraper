package com.yedam.inheritance;
/*
 * Parent의 클래스를을 Child가 상속클래스
 */
public class Child extends Parent {
	String filed2; // 필드
	
	
	//생성자 : 기본생성자를 생성함 = Child() => super() 
	
	public Child() {
		super("");
	}
	
	
	@Override//어노테이션 부모의 메소드 정의 ( 반환값, 메소드이름, 매개값)
	//부모가 가진 메소드를 재정의 하겠다 규칙을 지켜야한다
	void method1() {
		
		//부모의 메소드를  자삭이 재 정의
		//메소드 오버라이드라고함
		System.out.println("method2 호출");
	}

	void method2() {
		System.out.println("method2 호출");
	}


	@Override
	public String toString() {
		return "Child [filed2=" + filed2 + "]";
	}
	
	//toString() Override
	
}

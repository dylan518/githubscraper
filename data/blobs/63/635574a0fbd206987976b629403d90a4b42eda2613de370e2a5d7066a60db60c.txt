package sec01;

class Car{
	String color;
	int speed;
}

public class CarExample {

	public static void main(String[] args) {
		Car myCar1 = new Car(); // myCar1이라는 이름의 클래스객체 생성
		          //Car 클래스의 인스턴스(객체)를 생성하고 이를 myCar1이라는 이름의 변수에 할당
		
		//Car myCar1; //Car 타입의 myCar1이라는 이름의 변수를 선언만 함 
		//myCar1 = new Car(); //new Car()를 통해 Car 클래스의 새 인스턴스(객체)를 생성 후, 
		                      //이를 myCar1 변수에 할당
		myCar1.color = "red";
		myCar1.speed = 10;
	
		System.out.println("Color of Car1 is "+ myCar1.color + " and its speed is "+ myCar1.speed + "km.");
		
		
		Car myCar2 = new Car();
		myCar2.color = "blue";
		myCar2.speed = 20;
		
		System.out.println("Color of Car2 is "+ myCar2.color + " and its speed is "+ myCar2.speed + "km.");
	
	}
	
}

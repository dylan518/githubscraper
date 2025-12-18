package exam;

public class AppMain {

	public static void main(String[] args) {
		Student park = new Student("박경태", 3, 10_000);
		park.showInfo();
		// 버스		
		Bus bus100 = new Bus(100);
		bus100.showInfo();
		// 승객 승차 후
		park.takeBus(bus100);
		System.out.println("====== 학생 Park이 승차한 후 ======");
		park.showInfo();
		bus100.showInfo();
		Student kim = new Student("김경태", 6, 20_000);
		System.out.println("====== 학생 kim이 승차한 후 ======");
		kim.takeBus(bus100);
		kim.showInfo();
		bus100.showInfo();
	}

}

package week2_homework;


/**
 * 인간을 나타내는 간단한 클래
 * @author 임현
 *
 */
public class Human {
	
	private String name;
	private int age;
	
	/**
	 * 이름을 얻는다.
	 * @return 이름
	 */
	public String getName() {
		return name;

	}
	
	/**
	 * 이름을 설정한다.
	 * @param n 이름
	 */
	public void setName(String n) {
		this.name = n;

	}
	
	/**
	 * 나이를 설정한다.
	 * @param i 나
	 */
	public int getAge() {
		return age;
	}
	
	/**
	 * 나이를 설정한다.
	 * @param i 나
	 */
	public void setAge(int i) {
		this.age = i;
	}

	//@Override
	public String toString() {
		return "Human[name=" + name + ", age=" + age + "]";
	}
	
	//객체생성 메인 메소드
	public static void main(String[] args) {
		
		Human human1 = new Human();
		Human human2 = new Human();
		
		human1.setName("Yuri");
		human1.setAge(19);
		
		human2.setName("Cheolmin");
		human2.setAge(20);
		
		System.out.println(human1);
		System.out.print(human2);
	}

}
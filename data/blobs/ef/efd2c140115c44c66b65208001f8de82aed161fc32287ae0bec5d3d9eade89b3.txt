package D20240722;

public class StudentArrayEx01 {

	public static void main(String[] args) {
		int i1 = 10;
		int i2 = 20;
		int i3 = 30;
		int i[] = new int[3];
		Student stu1 = new Student(1, "정지원1", 181, true, 4);
		Student stu2 = new Student(2, "정지원2", 182, false, 4);
		Student stu3 = new Student(3, "정지원3", 183, false, 4);
		Student[] stu = new Student[3]; // 객체 배열
		stu[0] = new Student(1, "정지원1", 181, true, 4);
		stu[1] = new Student(2, "정지원2", 182, false, 4);
		stu[2] = new Student(3, "정지원3", 183, false, 4);
		System.out.println(stu[0].StudentNum); // 값 출력
		stu[0].setStudentName("정지원01"); // 값 수정
		System.out.println(stu[0].getStudentName());
		stu[0].print();
		
		
		
	}

}

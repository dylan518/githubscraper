package standard.java;

public class StaticExam {

	public static void main(String[] args) {
		
		MyMath2 mm2 = new MyMath2();
		int a = (int) mm2.add(2, 3);
		System.out.println(a);

	}

}

class MyMath2{
	long add(long a, long b) {
		return a+b;
	}
	
	static long add1(long a, long b) {
		return a+b;
	}
}
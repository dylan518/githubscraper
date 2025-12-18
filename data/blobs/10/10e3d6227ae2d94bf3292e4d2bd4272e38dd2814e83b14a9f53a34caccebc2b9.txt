package test.kishan;

public class TestSolution {
	public static void main(String args[]) {
		int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
		System.out.println("calling println method");
		TestSolution ts = new TestSolution();
		// ts.print1();
		printStatic();
		ts.printaArray(arr);
		System.out.println("sum" + ts.sumarray(arr));
		// System.out.print(ts.print1());
	}

	public static void printStatic() {
		System.out.println("The print method is called");
	}

	public void printaArray(int arr[]) {

		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i]);
		}
	}

	public int sumarray(int arr[]) {
		int sum = 0;
		for (int i = 0; i < arr.length; i++) {
			sum = sum + arr[i];
		}
		return sum;

	}
}

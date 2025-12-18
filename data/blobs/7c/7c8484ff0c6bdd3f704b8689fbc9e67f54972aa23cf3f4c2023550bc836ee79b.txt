package exception;
import java.util.Scanner;



public class ExceptionMain2 {
	private int x,y;
	
	Scanner sc = new Scanner(System.in);
	
	public void input() {
		System.out.println("x 입력 ; ");
		x = sc.nextInt();
		System.out.println("y 입력 :");
		y = sc.nextInt();
	}
	
	public void output() {
		if(y >= 0) {
		
		int mul = 1;
		for(int i=1;i<=y;i++) {
			mul = mul*x;
		}
		
		System.out.println(mul);
		}else {
			//System.out.println("y는 0보다 크거나 같아야 한다.");
			//개발자가 강제로 Exception 발생
			try {
				throw new Exception("y는 0보다 크거나 같아야 한다"); //에러를 던짐:throw
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	public static void main (String[] args) {
		
		ExceptionMain2 e = new ExceptionMain2();
		e.input();
		e.output();

		
	}

}


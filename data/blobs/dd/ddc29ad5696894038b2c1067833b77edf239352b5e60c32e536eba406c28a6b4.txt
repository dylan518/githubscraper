import java.util.Scanner;

public class Ex02while문제 {
	
	public static void main(String[] args) {
		
		//입력한 수가 10미만이면 계속 입력 가능하고 10이상이면 입력중지
		
		Scanner sc = new Scanner(System.in);
		
		
		//while 활용
		int a =0;
		while (a<10) {
			a = sc.nextInt();
		}
		
		while (true) {
			a = sc.nextInt();
			if (a>=10) {
				break;
			}
		}
		
		//do~while 활용
		
		do {
			if(a<10) {
			a=sc.nextInt();
			}else break;
		}while(true);
		
		do {
			a=sc.nextInt();
		}while (a>=10);
		
		sc.close();
	}
}

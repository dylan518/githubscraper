package practice;

import java.util.Scanner;

public class Dice {
//	주사위 게임
//	랜덤한 주사위 값을 뽑아서 입력한 값과 일치하는지 확인 반복문(scanner) (while) (if num1==num2 break)
//	값의 범위는 1~6 (int)(math.random()*6)+1
//	값을 맞출때까지 프로그램이 진행된다.

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int selectNumber=0; int diceNumber=0;
		boolean isTrue=true;
		
		System.out.println("주사위 숫자를 입력해주세요.");
		selectNumber=sc.nextInt();
		
		while(isTrue) {
			diceNumber=(int)(Math.random()*6)+1;
			
			
			
		}
	}
	
	
	
}

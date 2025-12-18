package testpm.test_08;

public class test08_06 {

	public static void main(String[] args) {
		// 7. 거스름돈 구하기   10000원짜리 0개, 1000원짜리 0 개, 100짜리 0개, 10짜리 0개
		//    조건 : /나 %연산자는 각각 최대 두 번씩 사용가능
		//    단, 거스름돈은 만천원이 최대 값이다. 
		int money = 4570;  // 가격
		int pay = 10000;  // 지불금액
		int rest = 0;  // 잔액
		for (int i = 10000; i >= 10; i /= 10) {
			rest = (pay - money) / i % 10;
			System.out.print(i + "원짜리 " + rest + "개, ");
		}
	}

}

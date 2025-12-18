package java0526;

public class Excercise5 {

//자연수 중에서 20번쨰 소수를 출력하
//자연수 중에서 제일 작은 소수는 2다 그리고 3,5,7, ... 이런 방식으로
//자연수의 소수는 무한하다. 따라서 자연수에서 20번째 소수도 반드시 존재함.
//구현방법
//1.자연수 2부터 소수인지 판별한다. 각 자연수의 약수의 개수를 구한다
//2.소수이면 소수의 순서를 기록한다
//3.순서가 20이면 그 소수를 출력한 후 종료한다
//4. 순서가 20이 아니면 자연수를 1 증가시킨 후 1번 과정을 반복한다.
	public static void main(String[] args) {// while,,for.,if
		int num = 3;
		int order = 1;
		int division = 0;

		while (true) { // 1. Num 의 약수의 개수를 구한
			for (int i = 2; i < num; i++) {
				if (num % i == 0) {
					++division;
				}
			}
			if (division == 0) {
				++order;
				System.out.println(num);
			}
			if (order == 20) {
				break;
			}
			division = 0;
			++num;
		}
		// 약수의 개수가 2이면 order를 1 증가시킨다.
		// oreder 20이면 while 문 종료하고, 아니면 num을 1증가시킨후 num에 대해 반복한
		System.out.println("자연수에서 " + order + "번째 소수는 " + num + "입니다");
	}

}

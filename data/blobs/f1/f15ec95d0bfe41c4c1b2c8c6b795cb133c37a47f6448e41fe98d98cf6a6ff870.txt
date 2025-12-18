package sub3;

import java.util.ArrayList;
import java.util.List;

/*
 * 날짜 : 2022/09/13
 * 이름 : 김진	우
 * 내용 : 자료구조 List 실습하기
 * 
 * List
 *  - 배열과 유사하지만 동적으로 생성되는 선형 자료구조
 *  - 
 */

public class ListTest {

	public static void main(String[] args) {

		// List 생성
		List<Integer> list = new ArrayList<>(); // ArrayList보다 List가 더 좋음

		// 데이터 입력
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		list.add(1, 6);
		list.remove(2); // 인덱스 번호
		
		// 데이터 출력 get()
		System.out.println("1번째 원소 : " + list.get(0));
		System.out.println("2번째 원소 : " + list.get(1));
		System.out.println("3번째 원소 : " + list.get(2));

		System.out.println(list);
		
		// List 크기 size()
		System.out.println("list 크기 : " + list.size());
		
		// List 반복문
		for(int n : list) {
			System.out.print(n + " ");
		}
		System.out.println();
		
		// 문자열 리스트
		List<String> people = new ArrayList<>(); // 문자열이기 때문에
		
		people.add("김유신");
		people.add("김춘추");
		people.add("장보고");
		people.add("강감찬");
		people.add("이순신");

		System.out.println(people);
		
		// 객체 리스트
		List<Apple> apples = new ArrayList<>();
		
		apples.add(new Apple("한국", 3000));
		apples.add(new Apple("미국", 2000));
		apples.add(new Apple("일본", 1000));
		
		// 한국사과
		// Apple apple = apples.get(0);
		// apple.show();
		
		// 미국사과
		// Apple apple = apples.get(1);
		// apple.show();
		
		// 일본사과
		// Apple apple = apples.get(2);
		// apple.show();
		
		
	}

}






















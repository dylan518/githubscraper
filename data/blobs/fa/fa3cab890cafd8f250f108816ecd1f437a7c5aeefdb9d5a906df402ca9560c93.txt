package chapter10;

import java.util.Calendar;
import java.util.Date;

//java.util 패키지
//: 자바의 표준 라이브러리 중 하나
// : 

// 시간 날짜 처리 클래스
//Date 클래스
// : 날짜와 시간을 표현
// : 현재의 밀리초 단위까지를 반환
// >> toString(): 현재 날짜 시간을 문자열로 반환
// >> getTime( : 


// Calender 클래스
// : 날짜와 시간을 처리하기 위한 추상 클래스
// >> getInstance(): 현재 날짜와 시간으로 설정된 Calendar 객체를 반환
// >> get(int field): 지정된 필드의 값을 반환
// >> set(int year, int month, int date): 연, 월, 일,


public class JavaUtil {
		public static void main(String[] args) {
			Date date = new Date();
			
			System.out.println(date.toString());
			System.out.println(date.getTime());
			
			Calendar cal  = Calendar.getInstance();
			int year = cal.get(Calendar.YEAR);
			int month = cal.get(Calendar.MONTH) + 1; 
			int day = cal.get(Calendar.DAY_OF_MONTH);
			
			System.out.println(year + "" + month + " " + day);
			
		}
}

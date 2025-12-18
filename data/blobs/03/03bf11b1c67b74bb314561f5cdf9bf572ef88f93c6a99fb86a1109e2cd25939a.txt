package trust;

public class Main {
	public static void isLeapYear(int year) {
		 boolean isLeapYear = false; 
		 if (year % 4 == 0) {
			 isLeapYear = true; 
			 if (year % 100 == 0) {
				 if (year % 400 == 0)
					 isLeapYear = true;
				 else
					 isLeapYear = false;
			 }
		 }
		 else
			 isLeapYear = false;
		 if (!isLeapYear)
			 System.out.println(year + " is a Non Leap year"); 
		 else
			 System.out.println(year + " is a Leap year"); 
	}
	public static void main(String[] args) {
		isLeapYear(2022); 
		isLeapYear(2020); 
	}
}

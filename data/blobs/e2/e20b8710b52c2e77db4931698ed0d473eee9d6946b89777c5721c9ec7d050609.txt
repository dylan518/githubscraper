package ex_241022_ch4_2;

public class Book {
	// 멤버, 속성, 필드 
	String title;
	String author;

	// 생성자 매개변수1개
	public Book(String t) { 
		this("", "");// 생성자
		title = t;
		author = "작자미상";
		
	}
	// 생성자 매개변수2개
	public Book(String t, String a) { // 생성자
		title = t;
		author = a;
	}
	public void showInfo() {
		System.out.println("책 제목 : " + this.title + ", 작가 : " + this.author);
		
	}

	public static void main(String[] args) {
		Book littlePrince = new Book("어린왕자", "생텍쥐페리");
		Book loveStory = new Book("춘향전");
		Book lsyAiBook = new Book("누구나 쉽게 이용할수 있는 Ai 입문서","이상용");
		lsyAiBook.showInfo();
		System.out.println(littlePrince.title + " " + littlePrince.author);
		System.out.println(loveStory.title + " " + loveStory.author);
		
	}
}







package com.test.java.ch09;

public class Ex02Polymorphism {
	public static void main(String[] args) {	
		Book2 book = new Book2(); 
		book.setTitle ("자바 기본문법");
		
		EBook2 ebook = new EBook2(); 
		ebook.setTitle("자바 알고리즘");
		
		ComicBook cbook = new ComicBook(); 
		cbook.setTitle("만화로 배우는 자바");
		
		AudioBook2 ab = new AudioBook2(); 
		ab.setTitle("음성지원: 자바 기본문법");
		ab.setVolume(50);
		
		Cart cart = new Cart(); 
		cart.add(book);
		cart.add(ebook);
		cart.add(cbook); 
		cart.add(ab);
		
		cart.printList(); 
	}
}

class Cart {
	private Book2[] books = new Book2[10];
	private int index;
	
	
	public void add (Book2 b) {
		books[index] = b; 
		index++;
	}
	
	public void printList() {
		for (int i=0; i<index; i++) {
			if(books[i] == null) {
				break;
			}
			System.out.println(books[i].getTitle());
			System.out.println(books[i].getFontColor());
			//System.out.println(books[i].getVolume());
		}
	}
}


class Book2 {
	String title; 
	String fontColor;
	int volume ; 
	
	/*public int getVolume() {
		return volume; 
	}*/
	
	public String getFontColor() {
		return fontColor;
	}
	
	public void setTitle(String title) {
		this.title = title; 
	}
	
	public String getTitle() {
		return title; 
	}

}

class ComicBook extends Book2 {
	private boolean color;
	
	public void setColor(boolean color) {
		this.color = color; 
	}
	
	public boolean isColor () {
		return color; 
	}
	
	@Override 
	public String getTitle() {
		return "[코믹북]" + title; 
	}
}

class EBook2 extends Book2 {
	private String fontColor; 
	
	public void setFontColor(String fontColor) {
		this.fontColor = fontColor;
	}
	
	@Override
	public String getFontColor() {
		return fontColor;
	}
	
	@Override
	public String getTitle() {
		return "[이북]" + title;
	}
}

class AudioBook2 extends Book2{
	private int volume; 
	
	public void setVolume (int volume) {
		this.volume = volume ; 
	}
	
	/*@Override
	public int getVolume () {
		return volume;
	}*/
	
	@Override
	public String getTitle() {
		return "[오디오북]" + title; 
	}
}


/*
문제 1.
(1) 컴파일 에러가 발생하지 않도록 수정하세요.

문제 2.
AudioBook 클래스를 추가하세요.
카트에 오디오북을 담으세요.
카트의 리스트 출력 시 오디오북은 [오디오북]책제목의 형식으로 출력되도록 코딩하세요. 
*/
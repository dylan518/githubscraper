package com.kh.practice.list.library.view;

import java.util.ArrayList;
import java.util.Scanner;

import com.kh.practice.list.library.controller.BookController;
import com.kh.practice.list.library.model.vo.Book;

public class BookMenu {
	private Scanner sc = new Scanner(System.in);
	private BookController bc = new BookController();
	
	public void mainMenu() {
		System.out.println("== Welcome KH Library ==");
		while(true) {
			System.out.println("=====***** 메인 메뉴 *****=====");
			System.out.println("1. 새 도서 추가");
			System.out.println("2. 도서 전체 조회");
			System.out.println("3. 도서 검색 조회");
			System.out.println("4. 도서 삭제");
			System.out.println("5. 도서명 오름차순 정렬");
			System.out.println("9. 종료");
			System.out.print("메뉴 번호 선택 : ");
			int menuNum = sc.nextInt(); sc.nextLine();
			if(menuNum==1) {
				insertBook();
			} else if(menuNum==2) {
				selectList();
			} else if(menuNum==3) {
				searchBook();
			} else if(menuNum==4) {
				deleteBook();
			} else if(menuNum==5) {
				ascBook();
			} else if(menuNum==9) {
				System.out.println("프로그램 종료");
				return;
			} else {
				System.out.println("잘못 입력하였습니다. 다시 입력해주세요.");
			}
		}
	}
	
	public void insertBook() {
		System.out.print("도서명 : ");
		String title = sc.nextLine();
		System.out.print("저자명 : ");
		String author = sc.nextLine();
		String categoryStr = "";
		while(true) {			
			System.out.print("장르 입력 (1. 인문 / 2. 자연과학 / 3. 의료 / 4. 기타) : ");
			int category = sc.nextInt();
			if(category==1) {
				categoryStr = "인문";
				break;
			} else if(category==2) {
				categoryStr = "자연과학";
				break;
			} else if(category==3) {
				categoryStr = "의료";
				break;
			} else if(category==4) {
				categoryStr = "기타";
				break;
			} else {
				System.out.println("다시 입력해주세요.");
			}
		}
		System.out.print("가격 : ");
		int price = sc.nextInt();
		Book b = new Book(title, author, categoryStr, price);
		bc.insertBook(b);
	}
	
	public void selectList() {
		ArrayList<Book> bookList = bc.selectList();
		if(bookList==null) {
			System.out.println("존재하는 도서가 없습니다.");
		} else {
			System.out.println("===== 도서 전체 조회 =====");
			for(int i=0; i<bookList.size(); i++) {
				System.out.println(bookList.get(i));
			}
		}
	}
	
	public void searchBook() {
		System.out.print("검색할 도서명 : ");
		String keyword = sc.nextLine();
		ArrayList<Book> searchList = bc.searchBook(keyword);
		if(searchList==null) {
			System.out.println("검색 결과가 없습니다.");
		} else {
			System.out.println("검색 결과");
			for(int i=0; i<searchList.size(); i++) {
				System.out.println(searchList.get(i));
			}
		}
	}
	
	public void deleteBook() {
		System.out.print("삭제할 도서명 : ");
		String title = sc.nextLine();
		System.out.print("삭제할 저자명 : ");
		String author = sc.nextLine();
		Book remove = bc.deleteBook(title, author);
		if(remove==null) {
			System.out.println("삭제할 도서를 찾지 못했습니다.");
		} else {
			System.out.println("성공적으로 삭제되었습니다.");
		}
	}
	
	public void ascBook() {
		bc.ascBook();
	}
}

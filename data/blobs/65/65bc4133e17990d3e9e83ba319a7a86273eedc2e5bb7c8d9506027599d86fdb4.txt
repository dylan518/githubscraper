package com.jslhrd.bbb;

import java.io.*;

public class Exam_02 {

	public static void main(String[] args) {
		File file = new File("C:/Users/김현규/JSL/data");
		// 폴더존재유무 판단
		if (!file.exists()) {
			file.mkdir();
		}
		try {
			Thread.sleep(3000);// 3초간 정지
		} catch (Exception e) {
		}
		File file2 = new File(file, "abc.txt");
		if (!file2.exists()) {
			try {
				file2.createNewFile();
			} catch (IOException e) {
				System.out.println("경로를 찾을수 없음");
			}
		}
		if (file2.canWrite()) {// 쓰기가 가능하면
			file2.setReadOnly();// 읽기전요으로 변경
		}
	}
}

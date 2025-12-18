package com.kh.day11.ioStream.inputStream;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

public class Eaxm_Read {

	public static void main(String[] args) {

		// InputStream : 추상클래스
		// Cannot instantiate the type InputStream
		// InputStream is = new InputStream();
		InputStream is = null;

		// Unhandled exception type FileNotFoundException
		// Checked Exception : 반드시 예외처리 해줘야 하는 Exception
		try {
			is = new FileInputStream("src/ioStream/inputStream.txt");
			int readByte;
			while (true) {
				readByte = is.read();	// 읽을게 없는 경우 -1을 반환
				// 없으면 빠져나가도록!
				if (readByte == -1) break;	
				System.out.print((char) readByte);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

}

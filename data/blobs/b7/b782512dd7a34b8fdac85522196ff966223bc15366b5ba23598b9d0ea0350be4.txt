package com.ohgiraffers.chap05.section01.array.level02.normal;

import java.util.Scanner;

public class Application1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("문자열을 하나 입력하세요 : ");
        String str = scanner.nextLine();
        char[] chars = str.toCharArray();
        System.out.print("검색할 문자를 하나 입력하세요 : ");
        char ch = scanner.next().charAt(0);
        int cnt = 0;

        for(int i = 0 ; i < chars.length ; i++){
            if(chars[i] == ch){
                cnt ++;
            }
        }
        System.out.println("입력하신 문자열 " + str + "에서 찾으시는 문자 " + ch + "는 " + cnt +"개입니다.");
    }
}

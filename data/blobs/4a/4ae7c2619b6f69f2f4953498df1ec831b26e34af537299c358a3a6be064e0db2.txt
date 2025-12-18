package org.coding.backJoon.silver.p1251;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;


/**
 * 해결하지 못하여 풀이 참고
 */
public class P1251 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        solution(str);
    }

    private static void solution(String str) {
        LinkedList<String> list = new LinkedList<>();
        for (int i = 2; i < str.length(); i++){
            for (int j = 1; j < i; j++){
                StringBuilder sb1 = new StringBuilder(str.substring(0, j));
                StringBuilder sb2 = new StringBuilder(str.substring(j, i));
                StringBuilder sb3 = new StringBuilder(str.substring(i));
                String str1 = sb1.reverse().toString();
                String str2 = sb2.reverse().toString();
                String str3 = sb3.reverse().toString();
                list.add(str1 + str2 + str3);
            }
        }

        Collections.sort(list);
//        System.out.println(list);
        System.out.println(list.pop());
    }
}

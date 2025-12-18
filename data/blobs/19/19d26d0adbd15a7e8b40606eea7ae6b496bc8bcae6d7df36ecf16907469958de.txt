package BaekJoon.P1343;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * https://www.acmicpc.net/problem/1343
 * [1343번: 폴리오미노]-Silver5
 */

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        str = str.replace("XXXX","AAAA");
        str = str.replace("XX","BB");

        if(str.contains("X")){
            System.out.println(-1);
        }else{
            System.out.println(str);
        }
    }
}

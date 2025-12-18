package com.javarush.task.task05.task0529;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/* 
Консоль-копилка
*/

public class Solution {
    public static void main(String[] args) throws Exception {

        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
        int summ = 0;

        while (true)
        {
            String inp = buffer.readLine();
            if (!inp.equals("сумма")) {
                int number = Integer.parseInt(inp);
                summ += number;
            }
            else {
                System.out.println(summ);
                break;
            }
        }
    }
}

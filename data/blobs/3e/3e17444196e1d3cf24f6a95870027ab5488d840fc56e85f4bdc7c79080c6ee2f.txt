package com.solved.yuk.etc.bronze;

import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class Bronze_2592 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int sum = 0, modeCount = 0, modeNum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < 10; i ++){
            int number = Integer.parseInt(br.readLine());
            sum+=number;
            int count = map.get(number) == null ? 1 : map.get(number)+1;
            map.put(number, count);

            if(count > modeCount){
                modeCount = count;
                modeNum = number;
            }
        }
        bw.write((sum/10)+"\n"+modeNum);

        bw.flush();
        bw.close();
    }
}

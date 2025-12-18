package Programmers.level0;

import java.util.Arrays;

public class 최빈값구하기 {
    public static void main(String[] args) {
//        System.out.println(solution(new int[]{1,2,3,3,3,4}));
        System.out.println(solution(new int[]{1,1,2,2,2,3,3}));
//        System.out.println(solution(new int[]{1}));

    }

    public static int solution(int[] array) {
        if(array.length ==1){
            return array[0];
        }
        int answer = 0;
        int[] answerArray = new int[array.length+1];
        int max = Integer.MIN_VALUE;
        int max_idx = 0;
        for(int i =0; i<array.length; i++) {
            answerArray[array[i]]++;
        }
        for(int i =0; i<answerArray.length; i++) {
            if(max < answerArray[i]){
                max = answerArray[i];
                max_idx = i ;
            }
        }
        int count = 0;
        for(int i =0; i<answerArray.length; i++){
            if(answerArray[i]==max){
                count++;
            }
        }
        if(count >1 ){
            return -1;
        }
        answer = max_idx;
        return answer;
    }
}
package com.abn.scalar.dsa.day27;

/*
Count pairs whose sum is a multiple of m
Given N array elements find count of pairs (i j) such that

(array[i] + array[j] ) % m = 0

i != j
 */
public class SumPairMultipleofNum {

    public int solve(int[] array, int M) {

        int[] freqArray = new int[M];

        int count = 0;
        int pair;

        for(int i = 0; i < array.length; i++) {

            int val = array[i] % M;
            if(val == 0) {
                pair = 0;
            } else {
                pair = M - val;
            }

            count =  count + freqArray[pair];
            freqArray[val] ++;
        }
        return count;
    }

    public static void main(String[] args) {

        SumPairMultipleofNum sumPairMultipleofNum = new SumPairMultipleofNum();
        System.out.println(sumPairMultipleofNum.solve(new int[] {2, 3, 4, 8, 6, 15, 5, 12, 17, 7, 18}, 6));
    }
}

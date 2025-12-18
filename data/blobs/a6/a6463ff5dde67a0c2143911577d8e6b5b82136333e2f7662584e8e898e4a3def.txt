package com.Ravi;


public class Min2D {
    public static void main(String[] args) {
        int[][] arr ={{23,5,3},
                {18,33,99},
                {20,30,40,50},
                {16,19}
        };
        System.out.println(min(arr));

    }
    static int min(int[][] arr){
        if (arr.length == 0){
            return -1;
        }
        int min = arr[0][0];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if(min > arr[i][j]){
                    min = arr[i][j];
                }
            }
        }
        return min;

    }
}

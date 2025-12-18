package Lecture_17;

import java.util.Arrays;

public class SecondLargest {
    public static void main(String[] args) {
        int[] arr = {40,10, 20, 30 , 50};
        int ans = secondLar(arr);
        System.out.println(ans);
    }
    static int secondLar(int[] arr){
        int largest = Integer.MIN_VALUE;
        int secondLargestt = Integer.MIN_VALUE;

        for(int i = 0; i < arr.length; i++){
            if(arr[i] > largest){
                largest = arr[i];
            }
        }

        for(int j = 0 ; j < arr.length; j++){
            if(arr[j] != largest){ //50>40&&40<50
                if(secondLargestt==Integer.MIN_VALUE){
                    secondLargestt=arr[j];
                }
                else if(arr[j]>secondLargestt)
                    secondLargestt = arr[j];
            }
        }

        return secondLargestt;
    }


}

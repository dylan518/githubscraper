package Sorting;

import java.util.*;

public class bubbleSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the length of Array : ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        for(int i = 0; i < n; i++ ){
            System.out.print("Enter element " + (i + 1) + " : " );
            arr[i] = sc.nextInt();
        }
        System.out.println("Original Array");
        System.out.println(Arrays.toString(arr));

        bSort(arr);
        sc.close();
    }

    public static void bSort(int[] arr){
        for(int i= 0; i < arr.length-1; i++){
            for(int j = 0; j < arr.length - 1 - i; j++){
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
        System.out.println("New Sorted Array");
        System.out.println(Arrays.toString(arr)); 
    }
}

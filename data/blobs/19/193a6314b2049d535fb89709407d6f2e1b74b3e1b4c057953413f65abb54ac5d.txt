package binarySearch;

import java.util.Scanner;

public class orderAgnostic {
    public static void main(String[] args) {
        //int[] arr = {1,4,7,12,14,17,23,27,29,35};
        int[] arr = {35,33,30,28,26,24,22,20,10,9,7,4,3};
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter element number: ");
        int target = sc.nextInt();
        if(Agnostic(arr, target, 0, arr.length-1)>=0){
            System.out.println("Element found at index "+Agnostic(arr, target, 0, arr.length-1));
        }
        else{
            System.out.println("Element not found");
        }
        sc.close();
    }

    public static int Agnostic(int[] arr,int target, int start , int end) {
        if(arr[start] <= arr[end]){
            return intro.BinarySearch(arr, target, start, end);
        }
        else{
            return reverseBinary.BinarySearch(arr, target, start, end);
        }
    }
}

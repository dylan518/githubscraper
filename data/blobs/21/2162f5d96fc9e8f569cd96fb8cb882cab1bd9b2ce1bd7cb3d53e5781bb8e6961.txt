package session2_loop_array;

import java.util.Scanner;

public class ConcatArray {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the size of the 1st array: ");
        int size1 = input.nextInt();
        int[] arr1 = new int[size1];
        for (int i = 0; i < size1; i++) {
            System.out.println("Enter the element "+i+" of the 1st array: ");
            arr1[i] = input.nextInt();
        }
        System.out.println("Enter the size of the 2nd array: ");
        int size2 = input.nextInt();
        int[] arr2 = new int[size2];
        for (int i = 0; i < size2; i++) {
            System.out.println("Enter the element "+i+" of the 2nd array: ");
            arr2[i] = input.nextInt();
        }
        int newSize = size1+ size2;
        int[] newArray = new int[newSize];
        for (int i = 0; i < size1; i++) {
            newArray[i] = arr1[i];
        }
        int j=0;
        for (int i = size1; i < newSize; i++) {
            newArray[i] = arr2[j];
            j++;
        }
        for (int i = 0; i < newSize; i++) {
            System.out.print(newArray[i] + " ");
        }
    }
}

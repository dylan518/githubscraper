package practic;

import java.util.Scanner;

public class Practic7 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        final int X = 1;
        final int Y = 2;
        final int Z = 3;
        System.out.println("Введите длину массива:");
        int len = in.nextInt();
        boolean flag = false;
        int[] myArray = new int[len];
        for(int i=0;i<len;i++){
            System.out.println("Введите " + (i+1) + " элемент массива:");
            myArray[i]= in.nextInt();
            if (myArray[i]==X || myArray[i]==Y || myArray[i]==Z){
                flag = true;
            }
        }
        System.out.println(flag ? "Данное значение имеется в константах": "Данное значение отсутствует в константах");

    }
}

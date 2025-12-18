package com.Arrrays;
import jdk.swing.interop.SwingInterOpUtils;

import java.io.*;
import java.util.*;

public class RMS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int arr [] = new int[size];
        int sqr = 0;
        float mean = 0;
        float root = 0;
        //for taking input
        for(int i = 0 ; i<arr.length; i++){
            arr [i]= sc.nextInt();
        }
        //for square
        for(int i= 0; i<arr.length; i++){
            sqr += Math.pow(arr[i], 2);

        }
        System.out.println(sqr);
        //calcualte mean
        mean = sqr/(float)size;
        System.out.println(mean);

        //calcualte root
        root = (float)Math.sqrt(mean);
        System.out.println(root);
    }

}

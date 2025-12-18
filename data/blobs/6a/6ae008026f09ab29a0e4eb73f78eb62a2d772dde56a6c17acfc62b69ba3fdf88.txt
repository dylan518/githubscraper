package com.v1;

import java.util.Random;

public class MyArray {
    int[] array;
    int len;
    int size;
    public MyArray(int size){
        int i;
        array = new int[size];
        for(i=0;i<=size*2/3;i++){
            array[i] = new Random().nextInt();
        }
        len = i;
        this.size = size;
    }
    public void insertArray(int inData,int inIndex){
        for(int i = len-1;i>=inIndex;i--){
            array[i+1] = array[i];
        }
        array[inIndex] = inData;
        len++;
    }
    public void delArray(int index){

    }
    public void print(){
        for(int i = 0;i<len;i++){
            System.out.print(array[i]+" ");
        }
    }
}

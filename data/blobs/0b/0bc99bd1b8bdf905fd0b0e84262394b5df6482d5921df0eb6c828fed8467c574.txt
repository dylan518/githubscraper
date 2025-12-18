package Algorithms;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.ArrayList;
public class QuickSort {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        StringTokenizer st= new StringTokenizer(str," ");
        ArrayList<Integer> arr = new ArrayList<>();
        for (;st.hasMoreTokens();){
            arr.add(Integer.parseInt(st.nextToken()));
        }
        Integer[] arr1=arr.toArray(new Integer[arr.size()]);
        quick_sort(arr1);
        for(int i =0; i<arr1.length;i++){
            System.out.print(arr1[i]+" ");
        }
        
        bw.flush();
        bw.close();
    
    }
    public static void quick_sort(Integer[] arr){
        quick_sort(arr, 0, arr.length-1);
    }
    public static void quick_sort(Integer[] arr, int start, int end){
        int part = partition(arr, start, end);
        if (start <part-1){
            quick_sort(arr,start,part-1);
        }
        if(part<end){
            quick_sort(arr,part,end);
        }
        return; 
    }

    public static int partition(Integer[] arr, int start, int end){
        int pivot = arr[(start+end)/2];
        while(start<=end){
            while(arr[start]<pivot) start++;
            while(arr[end]>pivot)end--;
            if(start<=end){
                swap(arr,start,end);
                start++;
                end--;
            }
        }
        return start;
    } 

    public static void swap(Integer[] arr, int start, int end){
        int temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
    }
}


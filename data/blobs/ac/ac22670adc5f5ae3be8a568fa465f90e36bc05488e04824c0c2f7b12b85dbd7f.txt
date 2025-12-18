package LEETCODE;

import java.util.Arrays;

public class covered_ranges {
    public static void main(String[] args) {
        int a = 2;
        int b =5;
        int c=Math.abs(a-b);
        Boolean [] arr = new Boolean[c+1];
       int [][] ranges = {{1,2},{3,4},{5,6}};
       int s=0;
       for(int i =0 ;i<ranges.length;i++){
           int si =ranges[i][0];
           int li=ranges[i][ranges[i].length-1];
           for(int k =si;k<=li;k++){
               System.out.println(k);

           }

       }
    }
}

package Codeforces;

import java.util.Arrays;
import java.util.Scanner;

public class Maximum_median {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        long k=sc.nextInt();
        Integer[]arr=new Integer[n];
        for (int i=0;i<n;i++)arr[i]=sc.nextInt();
        Arrays.sort(arr);
        int l=arr[n/2],p=1;
        for (int i=n/2+1;i<n;i++){
            if ((long)(arr[i]-arr[i-1])*p<=k){
                k-=(long)(arr[i]-arr[i-1])*p;
                p++;
                l=arr[i];
            } else break;
        }
        l+=k/p;
        System.out.println(l);
    }
}

package com.posh.leetcode_problems.contest_problems;

public class symmetric_integers {
    public static void main(String[] args) {

        System.out.println(countSymmetricIntegers(1,100));
    }

    public static int countSymmetricIntegers(int low, int high) {

        int i=low;
        int count=0;
        while(i<=high){
            if(sum_check(i)){
                count++;
            }

            i++;
        }
        return count;
    }

    public static boolean sum_check(int n){
        int count=0;
        int x = n;
        while(n>0){
            count++;
            n/=10;
        }
        if((count&1)==0){
           return give_sum(x,count);
        }
        return false;
    }

    public static boolean give_sum(int n,int count){

        int count1=0;
        int count2=0;
        int count3=1;
        while(n>0){
            int rem = n%10;
            if(count3>count/2){
                count2+=rem;
            }
            else{
                count1+=rem;
            }
            count3++;
            n/=10;
        }
        return count1==count2;
    }
}

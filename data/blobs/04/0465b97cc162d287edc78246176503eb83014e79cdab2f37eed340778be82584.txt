//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            long X = Long.parseLong(read.readLine());

            Solution ob = new Solution();
            System.out.println(ob.jumpingNums(X));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    static long max;
    static void findNum(long X,String ans){
        if(ans.equals("")==false && Long.parseLong(ans)<=X){
            for(int i=0;i<ans.length()-1;i++){
                if(Math.abs(ans.charAt(i)-ans.charAt(i+1))!=1){
                    return;
                }
            }
            max=Math.max(max,Long.parseLong(ans));
        }
        if(ans.equals("")==false && Long.parseLong(ans)>X){
            return;
        }
        for(int i=0;i<=10;i++){
            if(ans.equals("")){
                findNum(X,i+"");
            }else{
                int num=(int)(ans.charAt(ans.length()-1)-'0');
                if(Math.abs(num-i)==1){
                    findNum(X,ans+i+"");
                }
            }
        }
    }
    static long jumpingNums(long X) {
        if(X<10){
            return X;
        }
        max=0;
        // code here
        findNum(X,"");
        return max;
    }
};
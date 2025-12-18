import java.util.Arrays;
import java.util.Scanner;

public class H_23815 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long [] dp = new long[n+1];
        long [] skipdp = new long[n+1];
        dp[0] = 1;
        skipdp[0] = 1;
        for(int i=1; i<=n; i++){
            String left = sc.next();
            String right = sc.next();
            long leftVal = 0;
            long righVal = 0;
            long skipLeftVal = 0;
            long skipRightVal = 0;
            switch (left.charAt(0)){
                case '+':
                    leftVal =dp[i-1]+(left.charAt(1)-48);
                    skipLeftVal = skipdp[i-1]+(left.charAt(1)-48);
                    break;
                case'-':
                    leftVal =dp[i-1]-(left.charAt(1)-48);
                    skipLeftVal = skipdp[i-1]-(left.charAt(1)-48);
                    break;
                case'*':
                    leftVal =dp[i-1]*(left.charAt(1)-48);
                    skipLeftVal =skipdp[i-1]*(left.charAt(1)-48);
                    break;
                case'/':
                    leftVal =dp[i-1]/(left.charAt(1)-48);
                    skipLeftVal =skipdp[i-1]/(left.charAt(1)-48);
                    break;
            }
            switch (right.charAt(0)){
                case '+':
                    righVal =dp[i-1]+(right.charAt(1)-48);
                    skipRightVal =skipdp[i-1]+(right.charAt(1)-48);
                    break;
                case'-':
                    righVal =dp[i-1]-(right.charAt(1)-48);
                    skipRightVal =skipdp[i-1]-(right.charAt(1)-48);
                    break;
                case'*':
                    righVal =dp[i-1]*(right.charAt(1)-48);
                    skipRightVal = Math.max(skipdp[i-1]*(right.charAt(1)-48),skipdp[i]);
                    break;
                case'/':
                    righVal =dp[i-1]/(right.charAt(1)-48);
                    skipRightVal =skipdp[i-1]/(right.charAt(1)-48);
                    break;
            }
            skipdp[i] = Math.max(dp[i-1],Math.max(skipLeftVal,skipRightVal));
            dp[i] = Math.max(leftVal,righVal);
            if(dp[i]<= 0 ){
                dp[i] =-999999999;
            }
            if(skipdp[i]<=0 && dp[i]<=0){
                System.out.println("ddong game");
                return;
            }
        }
        /*for(int i=1; i<=n; i++){
            System.out.println(dp[i]+" "+skipdp[i]);
        }*/
        System.out.println(Math.max(dp[n],skipdp[n]));
    }
}

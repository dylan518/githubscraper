package Recursion;

public class PrintXPowerN {
    public static int Power(int x, int n){
        if(n==0){
            return 1;
        }
        return x* Power(x,n-1);

       
    }
    public static int powerOptimised(int a, int n){ //Space COmlexity= O(log n) Time Complexity=O(n)
        if(n==0){
            return 1;
        }
        int half= powerOptimised(a, n/2);
        
        if(n%2!=0){
            return a* half*half;

        }
        return half*half;

    }
    public static void main(String args[]){

        int x=2, n=10;
        System.out.println(Power(x, n));
        System.out.println(powerOptimised(2, 5));
    }
}

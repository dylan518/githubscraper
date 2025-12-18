package Rating1000;
import java.util.*;

//problem link = https://codeforces.com/problemset/problem/1521/A
public class NastiaAndNearlyGoodNumbers {
      public static void main(String[] args) {
            Scanner scn = new Scanner(System.in);
            int n = scn.nextInt();
            for(int tc = 1 ; tc <= n ; tc++){
                  Long a = scn.nextLong();
                  long b = scn.nextLong();
                  
                  if(b == 1){
                        System.out.println("NO");
                  }else{
                        System.out.println("YES");
                        System.out.println(Long.toString(a)+' '+ Long.toString(a*b) + ' ' + Long.toString(a*(b+1)));
                  }
            }
      }
}

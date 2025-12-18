//for hollow rectange 

package javalloop;
import java.util.Scanner;
public class patter2 {
    public static void main(String laptop[]){
      Scanner A=  new Scanner(System.in);
      int a=A.nextInt();
      int b=A.nextInt();
      for(int i=1;i<=a;i++){
        for(int j=1;j<=b;j++){
            if(i==1 || i==a|| j==1||j==b)
            System.out.print("*");
            else
            System.out.print(" ");
        }System.out.println();
      }



    }
    
}

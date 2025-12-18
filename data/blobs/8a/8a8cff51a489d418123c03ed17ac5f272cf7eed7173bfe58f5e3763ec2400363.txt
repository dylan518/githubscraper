import java.util.Scanner;
public class Mul{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int M=sc.nextInt();
        int N=sc.nextInt();
        int count=0;
        for(int i=M;i<=N;i++){
            if(i%3==0){
                count++;
            }
        }
        System.out.println(count);
    }
}
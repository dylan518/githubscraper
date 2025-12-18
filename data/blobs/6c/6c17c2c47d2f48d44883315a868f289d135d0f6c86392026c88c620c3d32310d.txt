import java.util.*;
public class hello{
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int s = 0 , p = 1;
		while(n>0){
		    s+=n%10;
		    p*=n%10;
		    n/=10;
		}
		System.out.format("%d",p-s);
	}
}
package MyWorks;
import java.util.Scanner;
import java.util.Stack;
public class StackDecimalToBinary {

	public static void main(String[] args) {
		Scanner s= new Scanner (System.in);
		  System.out.println("Enter the Element ");
	         int n=s.nextInt();
	 		Stack <Integer> stk = new Stack<Integer>();
	 		while(n!=0) {
	 			stk.push(n%2);
	 			n=n/2;
	 		}
 			System.out.println("Binary value ");
	 		while(!stk.isEmpty()) {
	 			System.out.print(stk.pop());
	 		}

	}

}

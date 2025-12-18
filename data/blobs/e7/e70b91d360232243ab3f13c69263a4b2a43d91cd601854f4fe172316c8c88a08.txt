package Example;
import java.util.Scanner;
public class Fibonacci {

	public static void main(String[] args) {
		Scanner src=new Scanner(System.in);
		System.out.println("Enter the value");
		int size=src.nextInt();
			int n1=-1;
			int n2=1;
			int result=n1+n2;
			while(result<=size) 
			{	
				System.out.println(n1+n2);
				n1=n2;
				n2=result;
				result=n1+n2;

			}

		}


	}

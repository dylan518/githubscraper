package stringprogram;
import java.util.Scanner;

public class String12Palindrome {
	 static boolean isPalindrome(String st) {
		 int n=st.length();
		 for(int i=0;i<n/2;i++)
		 {
			 if(st.charAt(i)!=st.charAt(n-i-1))
			 {
					return false;
			 }
		 }
		 return true;
	 }
		

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the String:");
		String st = sc.nextLine();
		boolean b= isPalindrome(st);
		if(b==true)
		{
			System.out.println(" The String is Palindrome" );
		}
		else {
			System.out.println("The is String is not palindrome");
		}

	}

	

}

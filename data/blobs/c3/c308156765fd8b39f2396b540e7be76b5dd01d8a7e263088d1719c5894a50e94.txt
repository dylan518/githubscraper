package packageone;

import java.util.Arrays;

public class asspalind
{

	public static void main(String[] args) 
	{
String s1="race";
String s2="care";

char c[]=s1.toCharArray();
char c1[]=s2.toCharArray();

Arrays.sort(c);
Arrays.sort(c1);

if(Arrays.equals(c, c1))
{
	System.out.println("Palindrome");
}
else
{
	System.out.println("not Palindrome");

}
	}

}

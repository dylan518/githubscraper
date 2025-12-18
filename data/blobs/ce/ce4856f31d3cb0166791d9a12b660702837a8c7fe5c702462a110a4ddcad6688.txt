import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner stdin=new Scanner(System.in);
	    String s=stdin.next();
	    int alpa[]=new int[26];
	    for(int i=0;i<s.length();i++){
	        alpa[(int)s.charAt(i)-97]++;
	    }
	    for(int i:alpa)
	        System.out.print(i+" ");
	}
}

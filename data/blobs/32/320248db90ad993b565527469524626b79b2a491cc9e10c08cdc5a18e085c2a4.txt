// WAP to count the occurence of a character in the string

public class Main
{   
    public static int countChar(String S, char c){
        S=S.toLowerCase();
		    int count=0;
		    for (int i=0;i<S.length();i++){
		         if (S.charAt(i)==c){
		             count++;
		         }
		    }
		    return (count);
    }
    
	  public static void main(String[] args) {
	    
		System.out.println(countChar("Malayalam",'m'));
	}
}

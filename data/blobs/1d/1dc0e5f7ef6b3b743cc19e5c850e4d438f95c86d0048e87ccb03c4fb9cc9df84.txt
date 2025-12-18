package StringHandling;

public class Immutability {

	public static void main(String[] args) {
		String str = new String("Himanshu");
		 str.concat("Singh");
		System.out.println(str);
		

		
		// Here str pointing to "Himanshu" and after concatenation a new object is being created
		// HimanshuSingh but there is no reference variable available to pointing it. So, basically there 
		// are no changes happen in str. It will print only Himanshu. 
		  // If we really want to print the new object after concatenation then we have to assign a reference
		// variable to it then we can print "HimanshuSingh" after concatenation.
		// This non changeable behavior is known as Immutability.
		
		String str1 = new String("Himanshu");
		 String str2 = str1.concat("Singh");
		System.out.println(str1);
		System.out.println(str2);
		
		
	}

}

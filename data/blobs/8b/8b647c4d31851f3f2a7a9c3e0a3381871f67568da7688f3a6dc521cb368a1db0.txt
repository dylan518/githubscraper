package hackathon;
import java.util.*;
public class question_19 {

	public static void main(String[] args) {
		//WJP to display number of occurrence of all character
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Enter your sentence: ");
	    String s = scanner.nextLine();
		System.out.println();
		s=s.replace(" ", " ");
		
		char array[]=s.toCharArray();
		 int count = 0;
	   Map<Character,Integer> map = new TreeMap<>();	 
		for(int i = 0; i< array.length; i++) {
			
			count = 0;
			for(int j = 0; j<array.length; j++) {
				if (array[i]==array[j]) {
					
					count++;
				}
			}
			
			map.put(array[i], count);		
		}
		
		System.out.println("number of occurrence of all character:");
		System.out.println(""+map);
		
		scanner.close();

	}

}

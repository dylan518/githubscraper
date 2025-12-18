
public class MaxOccuringCharacter {
	
	public static void main(String[] args) {
		String input = "Naga brahmam";
		maxOccuring(input); 
	}

	private static void maxOccuring(String input) {
		int[] charCount = new int[256];
		
		for(char c:input.toCharArray()) {
			charCount[c]++;
		}
		
		char maxChar = ' ';
		int maxCount = 0;
		
		for(int i=0;i<charCount.length;i++) {
			if(charCount[i]>maxCount) {
				maxCount = charCount[i];
				maxChar = (char)i;
			}
		}
		System.out.println("Max occurring character: " + maxChar);
        System.out.println("Number of occurrences: " + maxCount);
		
		
	}
	

}

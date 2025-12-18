import java.util.HashSet;

class Solution
{   
	static int findLongestConseqSubseq(int arr[], int N) {
	   	int length = Integer.MIN_VALUE;
	   	HashSet<Integer> elements = new HashSet<>();
	   	for (int i: arr) {
	       elements.add(i);
	   	}
	   	int tempLength;
	  
	   	for (int i: arr) {
	      if (!elements.contains(i - 1)) {
	          int j = i;
	          while (elements.contains(j)) {
	              j++;
	          }
	          
	          tempLength = j - i;
	          length = Math.max(length, tempLength);
	      }
	  	}
	  
	   return length == Integer.MIN_VALUE ? 1 : length;
	}
}

public class s1 {
	public static void main(String[] args) {
		int a[] = {2, 6, 1, 9, 4, 5, 3};
		int n = 7;
		System.out.println(Solution.findLongestConseqSubseq(a, n));
		int b[] = {1, 9, 3, 10, 4, 20, 2};
		int m = 7;
		System.out.println(Solution.findLongestConseqSubseq(b, m));
	}
}
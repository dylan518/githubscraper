public class Palindrome {

	public static boolean isPalindrome(String s)
	{
		int i = 0, j = s.length() - 1;

		while (i < j) {
			if (s.charAt(i) != s.charAt(j))
				return false;
			i++;
			j--;
		}

		return true;
	}

	public static void main(String[] args)
	{
		String s = "Racecar";
		s = s.toLowerCase();

		if (isPalindrome(s))
			System.out.print("It's a palindrome");
		else
			System.out.print("It's not a palindrome");
	}
}

// Have a pointer at the start of the string and the end of the string while the one at the start increments
// towards the end, the pointer at the end decrements and if the positions have the same value, then
// it will continue and if all the value equal, then it will print out "It's a palindrome"
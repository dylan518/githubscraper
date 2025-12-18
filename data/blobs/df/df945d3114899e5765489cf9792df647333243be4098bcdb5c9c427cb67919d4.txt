/** String processing exercise 2. */
public class UniqueChars {
    public static void main(String[] args) {  
        String str = args[0];
        System.out.println(uniqueChars(str));
    }

    /**
     * Returns a string which is identical to the original string, 
     * except that all the duplicate characters are removed,
     * unless they are space characters.
     */
    public static String uniqueChars(String s)
    {
        String ans = "";
        boolean add;
        for (int i = 0; i < s.length(); i++)
        {
            add = true;
            for (int j = 0; j < ans.length(); j++)
            {
                if (s.charAt(i) == ans.charAt(j)) //checks if char exists in ans
                {
                    add = false;
                }
            }
            if (add || s.charAt(i) == 32) // unique char or is equal to 32 (space)
            {
                ans = ans + s.charAt(i); 
            }
        }
        return ans;
    }
}
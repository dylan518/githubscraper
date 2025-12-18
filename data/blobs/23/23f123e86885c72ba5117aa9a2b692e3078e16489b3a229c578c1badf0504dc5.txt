/*  W.A.J.P to find all interleaving of given strings. 
The given strings are: WX YZ
The interleaving strings are: YWZX WYZX YWXZ WXYZ YZWX WYXZ
              */


import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Q18_StringInterleavingProgram {

    
    public static void generateInterleaving(String str1, String str2, String res, Set<String> results) {
        
        if (str1.isEmpty() && str2.isEmpty()) 
        {
            results.add(res);
            return;
        }

       
        if (!str1.isEmpty()) 
        {
            generateInterleaving(str1.substring(1), str2, res + str1.charAt(0), results);
        }

        
        if (!str2.isEmpty()) 
        {
            generateInterleaving(str1, str2.substring(1), res + str2.charAt(0), results);
        }
    }

    public static void main(String[] args) {
    	
        String str1 = "WX";
        
        String str2 = "YZ";
        
        Set<String> results = new HashSet<>();

        generateInterleaving(str1, str2, "", results);

       
        System.out.println("All interleavings of strings " + str1 +  "  and " + str2 + " are:");
        
        Iterator itr = results.iterator();
		
		while(itr.hasNext())
		{
			System.out.println(itr.next());
		}
    }
}

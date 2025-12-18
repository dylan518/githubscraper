/*
 345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
 */

package leetcodeQuestions;
public class reverseVowels {
    
    public static String reverse(String s){

        //String to store the result
        String res="";

        //Char array to store the result
        char a[]=new char[s.length()];

        //Converting String to array
        for(int i=0; i<s.length(); i+=1)
            a[i]=s.charAt(i);

        //Taking two pointers one from begining and one from end
        int i=0,j=s.length()-1;

        //Iterating over the array
        while(i<j){

            //Checking if no vowel is at ith index
            if(a[i]!='a'&&a[i]!='e'&&a[i]!='i'&&a[i]!='o'&&a[i]!='u'&&a[i]!='A'&&a[i]!='E'&&a[i]!='I'&&a[i]!='O'&&a[i]!='U') i+=1;

            //Checking if no vowel is present at jth index
            else if(a[j]!='a'&&a[j]!='e'&&a[j]!='i'&&a[j]!='o'&&a[j]!='u'&&a[j]!='A'&&a[j]!='E'&&a[j]!='I'&&a[j]!='O'&&a[j]!='U') j-=1;

            //If there is vowel at both the indexes then reverse them
            else{
                char temp=a[i];
                a[i]=a[j];
                a[j]=temp;
                i+=1; j-=1;
            }
        }

        //Converting array to string
        for(char k:a) res+=k;

        //Return result
        return res;
    } 

    //Main function
    public static void main(String[] args) {
        String s="IceCreAm";
        String res=reverse(s);
        System.out.println("Res:"+res);
    }
}

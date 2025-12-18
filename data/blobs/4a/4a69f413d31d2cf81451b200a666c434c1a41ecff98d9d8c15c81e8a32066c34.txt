// https://leetcode.com/problems/longest-nice-substring

class Solution {
    public String longestNiceSubstring(String s) {
        String st="",p="",m="";
        int max=Integer.MIN_VALUE;
        for(int i=0;i<s.length();i+=1)
        {
            char ch=s.charAt(i);
            ch=(Character.isLowerCase(ch))?Character.toUpperCase(ch):Character.toLowerCase(ch);
            if(s.contains(Character.toString(ch))==true)
            {
                st+=s.charAt(i);
                p=st;
            }
            else
            {
                s=s.substring(i);
                System.out.println(s);
                i=0;
                st="";
            }
            if(p.length()>max)
            {
                max=p.length();
                m=p;
            }
            
        }
        if(m.length()==1)return "";
        else return m;
    }
}
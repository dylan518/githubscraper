class Solution {
    public int lengthOfLongestSubstring(String s) {
        int mx=0;
        int left=0;
        int right=0;
        HashSet<Character> hset=new HashSet<>();
        while(right<s.length())
        {
            while(hset.contains(s.charAt(right))){
                hset.remove(s.charAt(left));
                left++;
               // hset.add();
            }
           
                
               hset.add(s.charAt(right)) ;
              
            
            int diff=right-left+1;
            mx=Math.max(mx,diff);
             right++;
        }
        return mx;
    }
}
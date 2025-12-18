class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n=s.length();
        int maxlen=0;
       Map<Character,Integer> chara=new HashMap<>();
       int left=0;
        for(int i=0;i<s.length();i++){
            if(!chara.containsKey(s.charAt(i))|| chara.get(s.charAt(i))<left){
                chara.put(s.charAt(i),i);
                maxlen=Math.max(maxlen,i-left+1);
            }else{
                left=chara.get(s.charAt(i))+1;
                chara.put(s.charAt(i),i);
            }

         
        }
        return maxlen;
    }
}
class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] subS=s.split(" ");
        if(subS.length!=pattern.toCharArray().length) return false;
        String[] arr=new String[26];
        Set<String> set=new HashSet<>();
        for(int i=0;i<pattern.length();i++){
            if(arr[pattern.charAt(i)-'a']==null) {
                arr[pattern.charAt(i)-'a'] =subS[i];
                if(set.contains(subS[i])) return false;
                else set.add(subS[i]);
            }
            else {
                if(!arr[pattern.charAt(i)-'a'].equals(subS[i])) return false;
        
            }
        }
        
        return true;
    }
}

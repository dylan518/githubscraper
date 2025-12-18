package LC_Code;


class Solution {
    private char[] ch;
    private String s;
    private int patternLength;
    public boolean wordPatternMatch(String pattern, String s) {
        ch = pattern.toCharArray();
        this.s = s;
        patternLength = ch.length;

        return dfs(0,0,new HashMap<Character,String>(),new HashSet<String>());

    }

    public boolean dfs(int index1, int index2, HashMap<Character,String>map, HashSet<String>set){
        if(index1 == patternLength){
            if(index2 == s.length()){
                return true;
            }else{
                return false;
            }
        }

        if(map.containsKey(ch[index1])){
            String temp = map.get(ch[index1]);

            if(index2 + temp.length() <= s.length() && s.substring(index2,index2+temp.length()).equals(temp)){
                return dfs(index1+1,index2+temp.length(),map,set);
            }else{
                return false;
            }
        }

        for(int i = index2+1; i <=s.length(); i++){
            String temp = s.substring(index2,i);
            if(!set.contains(temp)){
                map.put(ch[index1],temp);
                set.add(temp);
                if(dfs(index1+1,index2+temp.length(),map,set)){
                    return true;
                }
                map.remove(ch[index1]);
                set.remove(temp);
            }
        }
        return false;
    }
}
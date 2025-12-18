class Solution {
    public String longestCommonPrefix(String[] strs) {
        int lo = 0;
        int hi = Integer.MAX_VALUE;
        for(String s : strs) hi = Math.min(hi,s.length());
        if(hi==0) return "";
        while(lo<=hi){
            int mid = (lo+hi)>>>1;
            if(isPossible(strs,mid)) lo=mid+1;
            else hi = mid-1;
        }
        return strs[0].substring(0,lo-1);
    }
    public boolean isPossible(String[] strs, int mid){
        String prefix = strs[0].substring(0,mid);
        for(int i =1;i<strs.length;i++){
            if(!strs[i].startsWith(prefix)) return false;
        }
        return true;
    }
}
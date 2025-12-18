class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        int j = s.length() - 1, i = 0;

        while( i <= j){
            if(s.charAt(i) == s.charAt(j)){
                i++;
                j--;
            }else{
                return false;
            }
        }
        return true;
    }
}
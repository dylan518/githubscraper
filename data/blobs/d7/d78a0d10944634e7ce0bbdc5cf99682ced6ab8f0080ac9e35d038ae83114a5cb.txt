class Solution {
    public boolean halvesAreAlike(String s) {
        int vowelCount1 = 0, vowelCount2 = 0;
        char vowels[] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        HashSet<Character> hs = new HashSet();
        for(char c: vowels) hs.add(c);
        for(int i = 0; i < s.length(); i++){
            if(i < s.length()/ 2){
                if(hs.contains(s.charAt(i))){
                    vowelCount1++;
                }
            }
            else{
                if(hs.contains(s.charAt(i))){
                    vowelCount2++;
                }
            }
        }

        return vowelCount1 == vowelCount2;
    }
}

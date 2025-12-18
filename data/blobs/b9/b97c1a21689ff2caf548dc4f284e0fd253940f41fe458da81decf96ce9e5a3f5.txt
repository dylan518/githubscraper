import java.util.*;
class Solution {
    public int solution(String s) {
        String str = s;
        int result = 0;
        
        while(true){
            //남은 문자열이 1개이면 바로 반환
            if(str.isEmpty()) return result;
            else if(str.length()==1) return result+1;
            else{
                char now = str.charAt(0); 
                int same = 0, diff = 0, idx = 0;
                //same==diff가 될때까지 시행
                do{
                    if(idx==str.length()) break;
                    if(now==str.charAt(idx++)) same++;
                    else diff++;
                }while(same!=diff);
                
                result++;
                str = str.substring(idx,str.length());
            }
        }
    }
}


// leetcode 1678. Goal Parser Interpretation

/*
You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
*/

class Solution {
    public String interpret(String command) {

     StringBuilder sb = new StringBuilder();
        
        for(int i =0; i<command.length(); i++){
            if(command.charAt(i)=='G'){
                sb.append('G');
            }
            else if(command.charAt(i)=='(' && command.charAt(i+1)==')'){
                sb.append('o');
            }
            else if(command.charAt(i)=='(' && command.charAt(i+3)==')'){
                sb.append("al");
            }
        }

        return sb.toString();
        
    }
}

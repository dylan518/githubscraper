import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int solution(String myString, String pat) {

           String[] a = myString.split("");

            for(int i = 0; i < myString.length(); i++){
                if(a[i].equals("A")){
                    a[i] = "B";
                }else {
                    a[i] = "A";
                }
            }
            String b = Arrays.stream(a).collect(Collectors.joining());


            if(b.contains(pat)){
             return 1;
            }else {
                return 0;
            }

    }
}
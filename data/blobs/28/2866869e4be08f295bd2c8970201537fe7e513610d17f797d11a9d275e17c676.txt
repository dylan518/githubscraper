import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'pickingNumbers' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY a as parameter.
     */
    public static List<Integer> createSubArray(List<Integer> a,int b){
        //arrayList of subArray
        List<Integer> subArray = new ArrayList<>();
        
        //integer of subArray
        for(Integer integer: a){
            if( integer == b || integer +1 ==b){
                subArray.add(integer);
            }
        }
        return subArray;
    }

    public static int pickingNumbers(List<Integer> a) {
    // Write your code here
        int result =0, tempVal=0;
        List<Integer> subArray = new ArrayList<>();
        //resultArray
        List<Integer> resultArray = new ArrayList<>();
        
        for(int i =0; i< a.size();i++){
            //CreateSubArray function
            resultArray.add(createSubArray(a,a.get(i)).size());
        }
        
        System.out.println(resultArray);
        //integer of  resultArray
        for(Integer integer: resultArray){
            if(integer >=result){
                //assign integer to result
                result = integer;
            }
        }
        return result;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> a = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int result = Result.pickingNumbers(a);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

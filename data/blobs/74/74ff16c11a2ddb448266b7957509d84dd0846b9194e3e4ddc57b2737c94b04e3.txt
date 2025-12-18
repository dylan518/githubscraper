import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Solution {

    public static void main(String[] args) {
        List<Integer> ints = new ArrayList<>();
        try (BufferedReader fileReader = new BufferedReader(new FileReader(args[0]));){
          while (fileReader.ready()){
              ints.add(Integer.parseInt(fileReader.readLine()));
          }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        Collections.sort(ints);
        int m = ints.get(ints.size()/2);
        int result = 0;
        for (Integer anInt : ints) {
            result += Math.abs(anInt - m);
        }
        System.out.print(result);
    }


}

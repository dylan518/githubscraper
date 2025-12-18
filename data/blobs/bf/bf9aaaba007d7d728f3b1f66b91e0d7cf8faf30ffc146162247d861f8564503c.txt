package array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class PascalsTriangle_II {

    public static void main(String[] args) {
        List<Integer> generate = generate(3);

        for (Integer l:generate){
            System.out.println(l+" ");
        }
    }

    public static List<Integer> generate(int numRows) {

        Integer[] prev = new Integer[0];

        for (int i = 1; i <= numRows; i++) {

            Integer[] temp= new Integer[i];

            temp[0]=1;
            temp[i-1]=1;


            if(i>2) {
                int start=1;
                int end=i-2;
                while (start <= end) {
                    temp[start] = prev[start] + prev[start-1];
                    start++;

                    temp[end] = prev[end] + prev[end - 1];
                    end--;
                }
            }
            prev= temp;

        }

        return Arrays.stream(prev).toList();
    }

}

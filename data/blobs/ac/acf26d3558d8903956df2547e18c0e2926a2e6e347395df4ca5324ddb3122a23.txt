package median;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {

    /*
        [3,2, 2, 4] - [1,2,3,4]
        2 2 3 4        1 2 1 1

        [5, 5, 2, 3, 4, 1, 1, 2]   [1(2),2(2), 3(1), 4(1), 5(2)]   k = 4
        set {5, 2, 3, 4, 1,}
        1 1 2 2 3 4 5 5

        [3, 2, 2, 1, 1]    1(2) 2(2) 3(1)  n = 3
        1 1 2 2 3

                *
     */
    public static int median(Integer []tab) {
        int n = tab.length;
        int k = 0;
        if(n%2 == 1) {
            k = n / 2 + 1;
        } else {
            k = n / 2;
        }

        Set<Integer> set = new HashSet<>(Arrays.asList(tab));

        int []temp = new int[set.size() + 1];

        for(Integer el : tab) {
            temp[el] ++;
        }

        int sum = 0;
        for(int i = 0; i < temp.length; i++) {
            sum += temp[i];

            if(sum >= k) {
                return i;
            }
        }

        return -1;
    }
    public static void main(String[] args) {
        System.out.println(median(new Integer[]{5, 5, 2, 3, 4, 1, 1, 2}));
        System.out.println(median(new Integer[]{3, 2, 2, 1, 1}));

        //1 2 3 4 5 6 7
        System.out.println(median(new Integer[]{7, 5, 6, 3, 1, 2, 4}));
    }
}

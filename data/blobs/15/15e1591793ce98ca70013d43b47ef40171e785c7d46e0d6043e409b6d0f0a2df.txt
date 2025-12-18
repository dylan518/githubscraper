package dsaWithJava.functions.Array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

//https://leetcode.com/problems/find-the-highest-altitude/description/
public class FindTheHighestAltitude {
    public static void main(String[] args) {
        int[] gain = {-4,-3,-2,-1,4,3,2};
//        int ans = largestAltitude(gain);
        int ans2 = alternateSolution(gain);
        System.out.println(ans2);
    }

    static int largestAltitude(int[] gain) {
        ArrayList milestones = new ArrayList<>();
        milestones.add(0,0);
        int initial = 0;
        for (int i = 0; i < gain.length; i++) {
            initial = initial + gain[i];
            milestones.add(i+1,initial);
        }
        Collections.sort(milestones);
        int ans = (int) milestones.get(milestones.size() - 1);
        return ans;
    }

    static int alternateSolution(int[] gain){
        // Takes 0ms for computing as compared to above solution which takes 2ms.
        int sum = 0;
        int m = 0;
        for (int i = 0; i < gain.length; i++) {
            sum = sum + gain[i];
            m = Integer.max(m,sum);
        }
        return m;
    }
}

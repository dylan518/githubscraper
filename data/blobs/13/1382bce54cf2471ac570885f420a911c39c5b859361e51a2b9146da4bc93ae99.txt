package org.example.item59;

import java.util.Random;

public class RandomWithoutBug {

    static Random rnd = new Random();

    public static void main(String[] args) {
        int n = 2 * (Integer.MAX_VALUE / 3);
        int low = 0;
        for (int i = 0; i < 1000000; i++)
            if (rnd.nextInt(n) < n/2)
                low++;
        System.out.println(low);
    }
}

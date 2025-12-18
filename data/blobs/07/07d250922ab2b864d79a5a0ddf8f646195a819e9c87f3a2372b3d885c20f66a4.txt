package org.coursera;

import java.math.BigInteger;
import java.util.*;

public class FibonacciLastDigit {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        long c = findLastDigitOfFibonacci(BigInteger.valueOf(n));
        System.out.println(c);
    }

    public static int findLastDigitOfFibonacci(BigInteger n) {
        if (n.equals(BigInteger.ZERO)) {
            return 0;
        } else if (n.equals(BigInteger.ONE)) {
            return 1;
        } else {
            BigInteger a = BigInteger.ZERO;
            BigInteger b = BigInteger.ONE;
            BigInteger c = BigInteger.ZERO;
            BigInteger ten = BigInteger.TEN;
            for (BigInteger i = b.add(b); i.compareTo(n) <= 0; i = i.add(BigInteger.ONE)) {
                c = a.add(b).mod(ten);
                a = b;
                b = c;
            }
            return c.intValue();
        }
    }
}


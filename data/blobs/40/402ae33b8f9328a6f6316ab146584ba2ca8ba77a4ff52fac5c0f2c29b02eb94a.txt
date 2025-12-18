package com.algorithmen.math;

/*Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.
The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a
fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.*/
public class FractionAdditionAndSubtraction {
    //runtime beats 36% , memory 42%
    public String fractionAddition(String expression) {
        if (expression == null) {
            return "0";
        }

        String[] parts = expression.split("/|(?=[-+])");
        int numerator = 0;
        int denominator = 1;

        for (int i = 0; i < parts.length - 1; i += 2) {
            int currentNumerator = Integer.parseInt(parts[i]);
            int currentDenominator = Integer.parseInt(parts[i + 1]);

            // Reducing fractions to a common denominator
            numerator = numerator * currentDenominator + currentNumerator * denominator;
            denominator *= currentDenominator;

            // Reducing the fraction
            int gcd = gcd(Math.abs(numerator), denominator);
            numerator /= gcd;
            denominator /= gcd;
        }

        return numerator + "/" + denominator;
    }

    private int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}

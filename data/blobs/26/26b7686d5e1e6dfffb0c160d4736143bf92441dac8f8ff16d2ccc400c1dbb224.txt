package com.aslinformationservices.calculator;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
	 private static final double DELTA = 1e-15;

	    @Test
	    void testAdd() {
	        Calculator calculator = new Calculator();
	        assertEquals(5.0, calculator.add(2.0, 3.0), DELTA);
	    }

	    @Test
	    void testSubtract() {
	        Calculator calculator = new Calculator();
	        assertEquals(-1.0, calculator.subtract(2.0, 3.0), DELTA);
	    }

	    @Test
	    void testMultiply() {
	        Calculator calculator = new Calculator();
	        assertEquals(6.0, calculator.multiply(2.0, 3.0), DELTA);
	    }

	    @Test
	    void testDivide() {
	        Calculator calculator = new Calculator();
	        assertEquals(2.0, calculator.divide(6.0, 3.0), DELTA);
	    }

	    @Test
	    void testDivideByZero() {
	        Calculator calculator = new Calculator();
	        assertThrows(IllegalArgumentException.class, () -> calculator.divide(5.0, 0.0));
	    }

	    // Add more tests for edge cases and custom feature
	    // ...

	    @Test
	    void testEquationSolver() {
	        EquationSolver equationSolver = new EquationSolver();
	        assertEquals(2.0, equationSolver.solveLinearEquation(1.0, -3.0, -1.0), DELTA);
	    }

	    @Test
	    void testCustomFeatureMean() {
	        CustomFeature customFeature = new CustomFeature();
	        double[] numbers = { 1.0, 2.0, 3.0, 4.0, 5.0 };
	        assertEquals(3.0, customFeature.calculateMean(numbers), DELTA);
	    }

	    @Test
	    void testCustomFeatureMeanEmpty() {
	        CustomFeature customFeature = new CustomFeature();
	        double[] emptyArray = {};
	        assertThrows(IllegalArgumentException.class, () -> customFeature.calculateMean(emptyArray));
	    }

  
}
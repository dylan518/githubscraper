/***
	    	 * Algoritmos y Estructura de datos
	    	 * Michelle Mejía 22596
	    	 * Clase calculadora, realiza operaciones de aritmética básica.
	    	 *Utiliza el patrón de diseño SingleTon
	    	 */

package models;

import interfaces.ICalculator;

public class Calculator implements ICalculator {
	
	public static Calculator instance;
	
	
	/***
	 * @param float a and b
	 * @return the result of the addition
	 */
	@Override
	public float add(float a, float b) {
		return a+b;
	}
	
	/***
	 * @param float a and b
	 * @return the result of the subtraction
	 */
	@Override
	public float subtraction(float a, float b) {
		return a-b;
	}
	
	/***
	 * @param float a and b
	 * @return the result of the multiplication
	 */
	@Override
	public float multiplication(float a, float b) {
		return a*b;
	}
	
	/***
	 * @param float a and b
	 * @return the result of the division and 0 when a number is divided into 0.
	 */
	@Override
	public float division(float a, float b) {
		try {
			return b/a;
		}
		catch(Exception e3) {
			System.out.println("Existe una división inválida. Se ha retornado 0 como resultado.");
			return 0;
		}
	}

	@Override
	public void getNextImput() {
		
	}
	
	public static Calculator getInstance() {
		if (instance==null ) {
			instance = new Calculator();
		
		}
		return instance;
	}

}


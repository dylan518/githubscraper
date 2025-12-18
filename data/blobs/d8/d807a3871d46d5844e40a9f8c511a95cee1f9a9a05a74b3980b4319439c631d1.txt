/*
 Dada una cantidad de grados centígrados se debe mostrar su equivalente en grados Fahrenheit. 
La fórmula correspondiente es: F = 32 + (9 * C / 5).
 */
package ejercicio.pkg4;

import java.util.Scanner;

public class Ejercicio4 {

   
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int temp, faren;
        System.out.println("Ingrese los grados en celcius");
        temp = leer.nextInt();
        
        faren = (32 + (9 * temp / 5));
        
        System.out.println("Los temperatura es de " + faren + " fahrenheit.");
    }
    
}

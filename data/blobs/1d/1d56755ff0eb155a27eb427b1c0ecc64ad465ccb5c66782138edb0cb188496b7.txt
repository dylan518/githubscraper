/*Escribe un programa que tome como entrada un número entero e indique qué
 cantidad hay que sumarle para que el resultado sea múltiplo de 7 */

package ud1.exercicios.jcp20241010;

import java.util.Scanner;

public class EP0129 {
    public static void main(String[] args) {
        
        int numEntero, numResto, respuesta;
        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce un número entero");
        numEntero = sc.nextInt();
        sc.close();

        numResto = numEntero%7;
      
        respuesta = numEntero<7? 7-numEntero: numEntero ==7? 0 : 7-numResto;

        System.out.printf("Es necesario sumarle al número introducido %d para que sea múltiplo de 7", respuesta);
    }
    
}

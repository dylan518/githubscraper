/*
Modifica el ejercicio de la tabla de multiplicar, para que el número introducido por pantalla esté acotado entre 1 y 10. 
Dependiendo del número que introduzca el usuario mostraremos todas las tablas de multiplicar desde el número introducido por el usuario hasta la tabla de 10 inclusive.
Ejemplo: Si número =8
8x1=8
8x2= 16
…
9x1=9
9x2=18
…
10x1=10
10x2=20
...
Prueba a modificar el ejercicio para que cada tabla se muestre en horizontal, en vez de en vertical
 */
package tema4;

import java.util.Scanner;

public class Ej12 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner (System.in);
        int num;
        
        do {            
            System.out.println("Introduce un numero");
            num = teclado.nextInt();
        } while (num<1 || num>10);
        
        for (; num<11; num++) {
            System.out.println(" ");
            for (int tab = 0; tab < 11; tab++) {
                System.out.println(num + "x" + tab + "=" + num*tab);                
            }
        }
    }
}

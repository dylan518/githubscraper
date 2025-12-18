/*
 * Víctor Valverde Olmedo
 * Pedirá cantidad de reyes, y si hay repetidos lo cambiara por un numero
 */
package Capitulo7;
import java.util.Scanner;
public class C7EJ21 {
	public static void main (String args[]) {
    
    Scanner s = new Scanner(System.in);
		int[]n = new int[15];

    
    for(int i = 0; i < n.length; i++){
      n[i] = (int)(Math.random()*501);
      }
      
      
        for(int i = 0; i <n.length; i++){
          
              while(n[i]%5 !=0){
               n[i]++;
          }
            }
          System.out.println("");
        
        
        for(int num:n){
          System.out.print(num + " ");
          }
          s.close(); //Evitar errores
	}
}

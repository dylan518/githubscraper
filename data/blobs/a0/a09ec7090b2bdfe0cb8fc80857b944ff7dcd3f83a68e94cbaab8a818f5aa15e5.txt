/**
 * Realiza un conversor de euros a pesetas. La cantidad en euros que se quiere
convertir deberá estar almacenada en una variable.
 * 
 * 
 * @author Juan Ignacio Ruiz
*/
public class Ejercicio4 {
  public static void main(String[] args) {
    double euros = 100;
    int pesetas;
    pesetas = (int) (euros * 166.386);
    System.out.println(pesetas);
  }
}

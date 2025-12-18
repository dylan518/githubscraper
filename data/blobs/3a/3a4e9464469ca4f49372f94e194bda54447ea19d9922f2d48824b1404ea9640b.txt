package caja;

public class Caja{
    // variables
    int alto;
    int ancho;
    int profundo;
    
    // constructor
    public Caja(){
        System.out.println("se esta ejecutando un constructor...");
    }
    public Caja(int alto,int ancho, int profundidad){
        System.out.println("se esta ejecutando un constructor con argumentos...");
        this.alto = alto;
        this.ancho = ancho;
        this.profundo = profundidad;
    }
   public float calcularVolumen(){
       return this.ancho * this.alto * this.profundo;
   }
    
}


package com.loiane.cursojava.aula11.encapsulamento;


public class TesteCarro {
     public static void main(String[] args) {
        
        Carro van = new Carro();
        
        van.setMarca("Fiat");// atribui um valor ao atributo
        System.out.println(van.getMarca());// obtém um valor
        
 
    } 
}

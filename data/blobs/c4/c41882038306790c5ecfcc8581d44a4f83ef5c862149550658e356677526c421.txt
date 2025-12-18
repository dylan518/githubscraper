/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package hoteles.entidades;

/**
 *
 * @author chris
 */
public class Hotel1 extends Hotel  {
    
    protected Double precio;
    protected double superficie;
    protected boolean washRoom = true;
    protected boolean ascensor = true;
    protected boolean calefaccion = true;

    public Hotel1(Double precio, double superficie, Integer cantidadHabitaciones) {
        super(cantidadHabitaciones); //Cuando se utiliza la palabra super se envía el dato al padre o madre de esta clase. 
        this.precio = precio;
        this.superficie = superficie;
    }
    
    
}


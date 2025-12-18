/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import java.util.Objects;

/**
 *
 * @author DAMIANA
 */
public class Juegos {
    
    private String nombre;
    private double precio;

    public Juegos(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }
     @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Juegos juegos = (Juegos) obj;
        return Objects.equals(getNombre(), juegos.getNombre());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getNombre());
    }

}

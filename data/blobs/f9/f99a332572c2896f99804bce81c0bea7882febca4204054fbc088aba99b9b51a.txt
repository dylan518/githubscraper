/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DatosPelicula;

/**
 *
 * @author jaimegm
 */
public class Productora {

    private String nombre;
    private String presupuesto;

    public Productora() {
    }

    public Productora(String nombre, String presupuesto) {
        this.nombre = nombre;
        this.presupuesto = presupuesto;
    }

    public String getPresupuesto() {
        return presupuesto;
    }

    public void setPresupuesto(String presupuesto) {
        this.presupuesto = presupuesto;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Productora{" + "nombre=" + nombre + ", presupuesto=" + presupuesto + '}';
    }

    public void producir(String nombre) {
        System.out.println(this.nombre + " ha producido esta película ");
    }

}

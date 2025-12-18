/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

/**
 *
 * @author Jonathan
 */
public class Funcionario extends Usuario{
    private String fechaIngresoEmpresa;
    private double sueldo;

    public Funcionario(String fechaIngresoEmpresa, double sueldo, int id, String tipo, String nombre, String apellido, String direccion, int telefono, String correo, String fechaNacimiento) {
        super(id, tipo, nombre, apellido, direccion, telefono, correo, fechaNacimiento);
        this.fechaIngresoEmpresa = fechaIngresoEmpresa;
        this.sueldo = sueldo;
    }

    public Funcionario(){}

    public String getFechaIngresoEmpresa() {
        return fechaIngresoEmpresa;
    }

    public void setFechaIngresoEmpresa(String fechaIngresoEmpresa) {
        this.fechaIngresoEmpresa = fechaIngresoEmpresa;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
    

    
    
    
}

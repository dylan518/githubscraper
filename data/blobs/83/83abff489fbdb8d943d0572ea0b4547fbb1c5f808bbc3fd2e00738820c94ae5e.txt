/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.ups.barzallom_ramirezj_exameninterciclo;

/**
 *
 * @author casa
 */
public class DecBonificaciones extends DecoradorEmpleado {

    private int bonificaciones;

    public DecBonificaciones(IEmpleado empleado, int bonificaciones) {
        super(empleado);
        this.bonificaciones = bonificaciones;
    }

    @Override
    public double getSueldo() {
        double sueldo = super.getSueldo();

        if (empleado.getTipo().equals("Tiempo Completo")) {
            int bonoPorBonificacion = bonificaciones / 3; 
            sueldo += bonoPorBonificacion;

            int bonoRestante = bonificaciones % 3;
            if (bonoRestante > 0) {
                sueldo += bonoRestante * 0.40;
            }
        } else {
            int bonoPorBonificacion = bonificaciones / 2;
            sueldo += bonoPorBonificacion;
        }

        return sueldo;
    }

}

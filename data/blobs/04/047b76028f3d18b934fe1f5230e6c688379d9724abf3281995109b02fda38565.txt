/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;
import modelo.Habitacion;
import modelo.Reserva;
import modelo.Usuario;
import vista.MetodoDePagoV;
import vista.PagoV;
import vista.ReservaV;

/**
 *
 * @author estud
 */
public class MetodoDePagoC implements ActionListener {

    MetodoDePagoV metodoDePagoV = new MetodoDePagoV();

    
    Usuario usuario = new Usuario();
    Habitacion habitacion = new Habitacion();
    Reserva reserva = new Reserva();
    Date fecha1, fecha2;

    public MetodoDePagoC(MetodoDePagoV metodoDePagoV, Usuario usuario, Habitacion habitacion, Date fecha1, Date fecha2, Reserva reserva) {
        this.metodoDePagoV = metodoDePagoV;
        this.reserva=reserva;
        this.usuario=usuario;
        this.habitacion=habitacion;
        this.fecha1 = fecha1;
        this.fecha2 = fecha2;
        this.metodoDePagoV.cancelar.addActionListener(this);
        this.metodoDePagoV.continuar.addActionListener(this);
        this.metodoDePagoV.setExtendedState(6);
        this.metodoDePagoV.setVisible(true);
        this.metodoDePagoV.setDefaultCloseOperation(3);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (metodoDePagoV.lista.getSelectedItem().toString() != "") {
            if (e.getSource() == metodoDePagoV.continuar) {
                
                    if(metodoDePagoV.lista.getSelectedItem().toString().equals("Tarjeta")){
                        PagoV pv = new PagoV();
                        PagoC pc = new PagoC(pv, usuario, habitacion,"Tarjeta", fecha1, fecha2,reserva);
                        metodoDePagoV.setVisible(false);
                    }else if(metodoDePagoV.lista.getSelectedItem().toString().equals("Efectivo")){
                        PagoV pv = new PagoV();
                        PagoC pc = new PagoC(pv, usuario, habitacion, "Efectivo", fecha1, fecha2,reserva);
                        metodoDePagoV.setVisible(false);
                    }
            } 
             
        }


        if (e.getSource() == metodoDePagoV.cancelar) {
                ReservaV rV = new ReservaV();
                ReservaC resenaC = new ReservaC(rV, usuario, habitacion);
                metodoDePagoV.setVisible(false);

    }
}
}
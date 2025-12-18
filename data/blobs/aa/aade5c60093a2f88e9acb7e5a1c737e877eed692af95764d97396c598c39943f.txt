package Controlador;

import DAO.*;
import Vista.*;
import Modelo.*;
import Procesos.*;
import java.awt.event.*;

public class CC_GestionarTanque extends MouseAdapter implements ActionListener{
    
    IU_GestionarTanque vista;
    DAO_GestionarTanque crud;
    Solicitud s;
    Tanque t;
    
    public CC_GestionarTanque(IU_GestionarTanque et) {
        vista=et;
        vista.jbtnREFRESCAR.addActionListener(this);
        vista.jrbllenar.addActionListener(this);
        vista.jrbvaciar.addActionListener(this);
        vista.jbtnLLENAR.addActionListener(this);
        vista.jbtnVACIAR.addActionListener(this);
        vista.jtblSOLICITUDES.addMouseListener(this);
        vista.jtblTANQUES.addMouseListener(this);
        ProcesosGenerales.Presentacion(vista,"GESTIONAR TANQUE");
        vista.jrbllenar.setSelected(true);
        botonesEstado("Llenado");
        actualizarTabla();
    }

    void actualizarTabla(){
        DAO_GenerarSolicitud dao_gs = new DAO_GenerarSolicitud();
        dao_gs.mostrarTablaTanque(vista.jtblTANQUES);
        dao_gs.mostrarTablaSolicitudes(vista.jtblSOLICITUDES);
        vista.jtxtcantidadLlenado.setText("");
        vista.jtxtcantidadVaciado.setText("");
        vista.jlblserie.setText("");
    }
    
    void botonesEstado(String accion){
        if(accion.equals("Llenado")){
            vista.jtxtcantidadLlenado.setText("");
            vista.jlblfondollenar.setVisible(false);
            vista.jpanllenado.setVisible(true);
            vista.jtxtcantidadVaciado.setText("");
            vista.jlblfondovaciar.setVisible(true);
            vista.jpanvaciado.setVisible(false);
        }else{
            vista.jtxtcantidadLlenado.setText("");
            vista.jlblfondollenar.setVisible(true);
            vista.jpanllenado.setVisible(false);
            vista.jtxtcantidadVaciado.setText("");
            vista.jlblfondovaciar.setVisible(false);
            vista.jpanvaciado.setVisible(true);
        }
    }
    
    @Override
    public void actionPerformed(ActionEvent ae) {
        
        if(ae.getSource() == vista.jbtnREFRESCAR){
            actualizarTabla();
        }
        if(ae.getSource() == vista.jrbllenar){
            botonesEstado("Llenado");
        }
        if(ae.getSource() == vista.jrbvaciar){
            botonesEstado("Vaciado");
        }
        if(ae.getSource() == vista.jbtnLLENAR){
            
            String serie = vista.jlblserie.getText();
            int cantidad = Integer.parseInt(vista.jtxtcantidadLlenado.getText());
                       
            crud = new DAO_GestionarTanque();
            crud.lleado(serie,cantidad);          
            actualizarTabla();
        }
        if(ae.getSource() == vista.jbtnVACIAR){
            
            String serie = vista.jlblserie.getText();
            int cantidad = Integer.parseInt(vista.jtxtcantidadVaciado.getText());

            crud = new DAO_GestionarTanque();
            crud.vaciado(serie,cantidad);          
            actualizarTabla();    
        }
    }
    
    @Override
    public void mouseClicked(MouseEvent me){
        
        if(me.getSource() == vista.jtblTANQUES){
            
            int fila = vista.jtblTANQUES.getSelectedRow();
            int id = Integer.parseInt(vista.jtblTANQUES.getValueAt(fila,0).toString());

            crud = new DAO_GestionarTanque();
            t = crud.completarTanque(id);
            
            vista.jlblserie.setText(t.getSerie());
        }
        if(me.getSource() == vista.jtblSOLICITUDES){
            
            int fila = vista.jtblSOLICITUDES.getSelectedRow();
            int id = Integer.parseInt(vista.jtblSOLICITUDES.getValueAt(fila,0).toString());
            
            crud = new DAO_GestionarTanque();
            s = crud.completarSolicitud(id);
            
            vista.jtxtcantidadLlenado.setText(""+s.getCantidad());
        }
    }   
}

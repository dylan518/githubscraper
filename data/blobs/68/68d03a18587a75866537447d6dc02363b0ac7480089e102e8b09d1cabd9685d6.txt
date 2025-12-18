/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package taller.data;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import javax.swing.JOptionPane;
import taller.entidades.Bicicleta;
import taller.entidades.Cliente;
import taller.entidades.Repuesto;

/**
 *
 * @author canes
 */
public class Bicicletadata {
   private Connection com;
   private ClienteData cli;

    public Bicicletadata() {
        this.com = Conexion.buscarconexion();
        this.cli = new ClienteData();
    }

    
    
    public void guardarBicicleta(Bicicleta bicicleta){
        String sql="INSERT INTO bicicleta (num_serie, tipo, color, dueño, estado) VALUES (?, ?, ?, ?,?)";
        try {
            PreparedStatement ps=com.prepareStatement(sql);
            ps.setInt(1, bicicleta.getNum_serie());
            ps.setString(2,bicicleta.getTipo());
            ps.setString(3,bicicleta.getColor());
            ps.setInt(4, bicicleta.getDueño().getDni());
            ps.setBoolean(5, bicicleta.isEstado());
            ps.executeUpdate();
                                   
                JOptionPane.showMessageDialog(null, "Bicicleta agregado exitosamente!");           
                     
            ps.close();           
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(null, "Bicicleta no se pudo agregar!");
                       
        }
    }
    
    public ArrayList<Bicicleta> obtenerBicletas(int dni){
        
        ArrayList<Bicicleta> listaBicicletas=new ArrayList();
        
        String sql="SELECT * FROM bicicleta WHERE estado = 1 AND dueño=? ";
        
        try {
            PreparedStatement ps=com.prepareStatement(sql);
            ps.setInt(1, dni);
            ResultSet rs=ps.executeQuery();
            
            while(rs.next()){
            
                Bicicleta b=new Bicicleta();
                
          b.setNum_serie (rs.getInt("num_serie"));
          b.setTipo(rs.getString("tipo"));
          b.setColor(rs.getString("color"));
          b.setDueño(cli.ObtenerclienteporDni(rs.getInt("dueño")));
          b.setEstado(rs.getBoolean("num_serie"));
                
                listaBicicletas.add(b);
            }
            
            ps.close();
            
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(null, "Error al obtener Bicicleta");
        }
    return listaBicicletas;
    }
    
    public Bicicleta obtenerBicleta(int num_serie){
               
        String sql="SELECT * FROM bicicleta WHERE estado = 1 AND num_serie=? ";
         Bicicleta b=null;
        try {
            PreparedStatement ps=com.prepareStatement(sql);
            ps.setInt(1, num_serie);
            ResultSet rs=ps.executeQuery();
            
            if(rs.next()){
            b= new Bicicleta();
                
          b.setNum_serie (rs.getInt("num_serie"));
          b.setTipo(rs.getString("tipo"));
          b.setColor(rs.getString("color"));
          b.setDueño(cli.ObtenerclienteporDni(rs.getInt("dueño")));
          b.setEstado(rs.getBoolean("num_serie"));
            }
            ps.close();
            
        } catch (SQLException ex) {
            JOptionPane.showMessageDialog(null, "Error al obtener Bicicleta");
        }
    return b;
    }
    
    
    
    
    public void borrarBicicleta (int num_serie){
        String sql="UPDATE `bicicleta` SET estado =0 WHERE num_serie=?";
        try {
            PreparedStatement ps=com.prepareStatement(sql);
            ps.setInt(1, num_serie);
            ps.executeUpdate();//
            
            JOptionPane.showMessageDialog(null, "Se elimino la bicicleta correctamente");
            
            ps.close();
            
    }   catch (SQLException ex) {
            JOptionPane.showMessageDialog(null, "BicicletaData Sentencia SQL erronea-borrar bicicleta");
        }
    }
    public void actualizarBicicleta(Bicicleta bici) {
        String sql = "UPDATE bicicleta SET num_serie= ? , tipo= ? ,color= ? ,dueño= ?, estado=? WHERE num_serie = ?";
            
            try {
            PreparedStatement ps = com.prepareStatement(sql);
            ps.setInt(1, bici.getNum_serie());
            ps.setString(2, bici.getTipo());
            ps.setString(3, bici.getColor());
            ps.setInt(4, bici.getDueño().getDni());
            ps.setBoolean(5, bici.isEstado());
            ps.setInt(6, bici.getNum_serie());
           
           
            if (ps.executeUpdate() > 0) {
                JOptionPane.showMessageDialog(null, "Se pudo actualizar la bicicleta.");
            } else  {
                JOptionPane.showMessageDialog(null, "No se pudo actualizar la bicicleta.");
            }
            
            ps.close();
            
        } catch(SQLException ex) {
            JOptionPane.showMessageDialog(null, "Se produjo un error. en actualizar bicicleta"+ex);
        }  
            }
  
            
    
}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Datos;
import Conexion.Conexion;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
/**
 *
 * @author JeTf
 */
public class DEspecialidad {
    private int idespecialidad;
    private String nombre;
    
    private Conexion conexion;
    private Connection con=null;

    public void setIdespecialidad(int idespecialidad) {
        this.idespecialidad = idespecialidad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getIdespecialidad() {
        return idespecialidad;
    }

    public String getNombre() {
        return nombre;
    }
    
    public void agregar(){
        conexion   = new Conexion();
        con        = conexion.conectar();
        PreparedStatement ps 
                   = null;
        String sql = "INSERT INTO especialidad (nombre) VALUES (?);";
        
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1, this.nombre);
            ps.execute();
            System.out.println("Especialidad Insertado exitosamente...");  
        } catch (Exception e) {
            System.out.println(" Error al Insertar Especialidad... "+ e.getMessage());
        }finally{
            try {
                con.close();
            } catch (Exception e) {
                System.err.println(e);
            }
        }
    }
     public void eliminar(){
        conexion    = new Conexion();
        con         = conexion.conectar();
        PreparedStatement ps 
                    = null;
        String sql  = "DELETE FROM especialidad WHERE idespecialidad="+this.idespecialidad;
         try {
             ps= con.prepareCall(sql);
             ps.execute();
             ps.close();
             System.out.println("Especialidad Eliminado exitosamente...");
         } catch (Exception e) {
             System.out.println("Error al Elimar Especialidad... ");
         }
     }
     
    public ArrayList listar(){
        conexion    = new Conexion();
        con         = conexion.conectar();
        PreparedStatement ps    = null;
        ArrayList<Object[]> esp = new ArrayList<>();
        String sql              = "SELECT *FROM especialidad";
        try {
            ps= con.prepareCall(sql);
            ResultSet r;
            r= ps.executeQuery();
            while (r.next()) {                
                esp.add( new  Object[]{
                r.getInt(1),//id
                r.getString(2)
                });
                System.out.println("lis "+ r.getInt(1)+" " +r.getString(2));
            }
           System.out.println("listando Especialidades... "); 
        } catch (Exception e) {
            System.out.println("Error al listar....");
            return null;
        }
        return esp;
    } 
    public void modificar(){
        conexion   = new Conexion();
        con        = conexion.conectar();
        PreparedStatement ps 
                   = null;
        String sql = "UPDATE especialidad SET nombre=? WHERE idespecialidad="+this.idespecialidad;
        try {
            ps= con.prepareStatement(sql);
            ps.setString(1, this.nombre);
            ps.execute();
            ps.close();
            System.out.println("modificador exitosamente");
        } catch (Exception e) {
            System.out.println("error al modificar.."+e.getMessage());
        }
    } 
}//fin class

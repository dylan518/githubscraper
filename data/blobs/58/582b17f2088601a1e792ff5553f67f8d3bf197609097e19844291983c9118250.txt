/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo;

import Conexion.ConexionPG;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Christian
 */
public class ModeloPersona {
    ConexionPG cpg = new ConexionPG();
    
    public ModeloPersona() { 
    }
    
    public List<Persona> enlistaPersonas() {
        List<Persona> listaPersonas = new ArrayList<>();
        String sql = "SELECT cedula, primnombre, segnombre, apellidopat, apellidomat, telefono"
                + ", direccion, emailper, genero, fechanacim\n" +
        "FROM public.persona;";
        ResultSet rs = cpg.Consultas(sql);
        try {
            while(rs.next()) {
                Persona persona = new Persona();
                
                persona.setCedula_per(rs.getString("cedula"));
                persona.setPrimeNombre_per(rs.getString("primnombre"));
                persona.setSegundoNombre_per(rs.getString("segnombre"));
                persona.setApellidoPat_per(rs.getString("apellidopat"));
                persona.setApellidoMat_per(rs.getString("apellidomat"));
                persona.setTelefono_per(rs.getString("telefono"));
                persona.setDireccion_per(rs.getString("direccion"));
                persona.setEmail_per(rs.getString("emailper"));
                persona.setGenero_per(rs.getString("genero"));
                persona.setFechaNacimiento_per(rs.getDate("fechanacim"));
                         
                listaPersonas.add(persona);
            }  
            rs.close();
            return listaPersonas;
        } catch (SQLException ex) {
            Logger.getLogger(ModeloPersona.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }
        
    }
    
    public boolean crearPersona(Persona p) { 
        String sql = "INSERT INTO public.persona(\n" +
        "cedula, primnombre, segnombre, apellidopat, apellidomat, telefono, direccion, emailper, "
        + "genero, fechanacim)\n" +
        "VALUES ('"+p.getCedula_per()+"', '"+p.getPrimeNombre_per()+"', '"+p.getSegundoNombre_per()+"', '"+p.getApellidoPat_per()+"', "
        + "'"+p.getApellidoMat_per()+"', '"+p.getTelefono_per()+"+', '"+p.getDireccion_per()+"',"
        + "'"+p.getEmail_per()+"', '"+p.getGenero_per()+"', '"+p.getFechaNacimiento_per()+"');";
        
        return cpg.CRUD(sql);
        
    }
    
    public Persona consultarPersona(String cedula) {
        Persona persona = new Persona();
        String sql = "SELECT cedula, primnombre, segnombre, apellidopat, apellidomat, telefono, direccion, emailper, genero, fechanacim\n" +
                    "FROM public.persona\n" +
                    "WHERE cedula = '"+cedula+"';";
        ResultSet rs = cpg.Consultas(sql);   
        
        try {
            while(rs.next()) {
                persona.setCedula_per(rs.getString("cedula"));
                persona.setPrimeNombre_per(rs.getString("primnombre"));
                persona.setSegundoNombre_per(rs.getString("segnombre"));
                persona.setApellidoPat_per(rs.getString("apellidopat"));
                persona.setApellidoMat_per(rs.getString("apellidomat"));
                persona.setTelefono_per(rs.getString("telefono"));
                persona.setDireccion_per(rs.getString("direccion"));
                persona.setEmail_per(rs.getString("emailper"));
                persona.setGenero_per(rs.getString("genero"));
                persona.setFechaNacimiento_per(rs.getDate("fechanacim"));   
            }
            rs.close();
            return persona;
        } catch (SQLException ex) {
            Logger.getLogger(ModeloPersona.class.getName()).log(Level.SEVERE, null, ex);
            return null;
        }
        
    }
    
    public boolean editarPersona(Persona p) {
        String sql = "UPDATE public.persona\n" +
        "SET primnombre='"+p.getPrimeNombre_per()+"','"+p.getSegundoNombre_per()+"', apellidopat='"+p.getApellidoPat_per()+"', "
                + "apellidomat='"+p.getApellidoMat_per()+"', telefono='"+p.getTelefono_per()+"', direccion='"+p.getDireccion_per()+"', "
                + "emailper='"+p.getEmail_per()+"', genero='"+p.getGenero_per()+"', fechanacim='"+p.getFechaNacimiento_per()+"'\n" +
        "WHERE cedula = '"+p.getCedula_per()+"';";   
        return cpg.CRUD(sql);
    }
    
    
    public boolean removerPersona(String cedula) {
        String sql = "DELETE FROM public.persona\n" +
                    "WHERE cedula = '"+cedula+"';;";   
        return cpg.CRUD(sql);
    }
    
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package estancias.persistencia;

import estancias.entidades.Casa;
import estancias.entidades.Cliente;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;

/**
 *
 * @author brunopc
 */
public final class ClienteDaoExt extends DAO{
    public Collection<Cliente> clientesYCasas(Date fecha,int dias) throws Exception{
        try {
            Collection<Casa> casasDisp = new ArrayList();
            Collection<Cliente> clientes = new ArrayList();
            Casa casa = null;
            Cliente cliente = null;
            
            String sql = "SELECT c.*,ca.* FROM clientes c inner join estancias e on c.id_cliente = e.id_cliente inner join "
                    + " casas ca on e.id_casa = ca.id_casa";
            consultarBase(sql);
            while(resultado.next()){
                casa = new Casa();
                cliente = new Cliente();
                cliente.setId_cliente(resultado.getInt(1));
                cliente.setNombre(resultado.getString(2));
                cliente.setCalle(resultado.getString(3));
                cliente.setNumero(resultado.getInt(4));
                cliente.setCodigo_postal(resultado.getString(5));
                cliente.setCiudad(resultado.getString(6));
                cliente.setPais(resultado.getString(7));
                cliente.setEmail(resultado.getString(8));
                casa.setId_casa(resultado.getInt(9));
                casa.setCalle(resultado.getString(10));
                casa.setCodigo_postal(resultado.getString(11));
                casa.setCiudad(resultado.getString(12));
                casa.setFecha_desde(resultado.getDate(13));
                casa.setPais(resultado.getString(14));
                casa.setFecha_hasta(resultado.getDate(15));
                casa.setTiempo_minimo(resultado.getInt(16));
                casa.setTiempo_maximo(resultado.getInt(17));
                casa.setPrecio_habitacion(resultado.getDouble(18));
                casa.setTipo_vivienda(resultado.getString(19));
                casasDisp.add(casa);
                clientes.add(cliente);
                
            }
            return clientes;
        } catch (Exception e) {
            throw e;
        }
        
        
    }
    public Cliente buscarPorCasa(Casa casa) throws Exception{
        try {
           
            Cliente cliente = null;
            
           String sql = "SELECT c.* FROM clientes c inner join estancias e on c.id_cliente = e.id_cliente inner join "
                    + " casas ca on e.id_casa = ca.id_casa WHERE ca.id_casa = " + casa.getId_casa();
            consultarBase(sql);
            if(resultado.next()){
                cliente = new Cliente();
                cliente.setId_cliente(resultado.getInt(1));
                cliente.setNombre(resultado.getString(2));
                cliente.setCalle(resultado.getString(3));
                cliente.setNumero(resultado.getInt(4));
                cliente.setCodigo_postal(resultado.getString(5));
                cliente.setCiudad(resultado.getString(6));
                cliente.setPais(resultado.getString(7));
                cliente.setEmail(resultado.getString(8));
            }
            
            return cliente;
        } catch (Exception e) {
            throw e;
        }
    }
    
}

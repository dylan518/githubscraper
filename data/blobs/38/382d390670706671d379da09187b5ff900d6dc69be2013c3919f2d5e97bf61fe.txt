package controlador;

import static java.awt.image.ImageObserver.HEIGHT;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JOptionPane;
import modelo.claseConexion;
import modelo.claseMarca;
import modelo.claseUsuario;
import modelo.claseVehiculo;


public class claseControladorVehiculo {
    private claseConexion conexionBD = new claseConexion();
    
    public List listar (){
        List<claseVehiculo> listarVehiculo = new ArrayList<>();
        PreparedStatement consulta;
        ResultSet datos;
        try {
            Connection miConexion = conexionBD.getConnection();
            String sql = "SELECT tbl_vehiculo.placa,tbl_vehiculo.idCliente,tbl_cliente.nombre as nomCliente,"
                    + "tbl_vehiculo.codMarca, tbl_marca.nombre as nomMarca,"
                    + "tbl_vehiculo.modelo,tbl_vehiculo.color "
                    + "FROM tbl_vehiculo,tbl_cliente,tbl_marca "
                    + "WHERE tbl_vehiculo.idCliente = tbl_cliente.identificacion and tbl_vehiculo.codMarca = tbl_marca.codigo;";
            consulta = miConexion.prepareStatement(sql);
            datos = consulta.executeQuery();

            while (datos.next()) {
                claseVehiculo vehiculo = new claseVehiculo();

                vehiculo.setPlaca(datos.getString("placa"));
                vehiculo.setIdCliente(datos.getInt("idCliente"));
                vehiculo.setNombre_cliente(datos.getString("nomCliente"));
                vehiculo.setCodMarca(datos.getInt("codMarca"));
                vehiculo.setNombre_marca(datos.getString("nomMarca"));
                vehiculo.setModelo(datos.getInt("modelo"));
                vehiculo.setColor(datos.getString("color"));
                
                listarVehiculo.add(vehiculo);
            }
            return listarVehiculo;
        } catch (SQLException er) {
            System.err.println("No se pudo conectar o hacer la consulta. " + er.getMessage());
            return listarVehiculo;
        }finally{
            conexionBD.setDesconectar();
        }
    }
    
    public void agregar (claseVehiculo ve){
        try {
            Connection miConexion = conexionBD.getConnection();
            
            String sql = "INSERT INTO tbl_vehiculo(color, idCliente, codMarca, modelo, placa) VALUES (?,?,?,?,?)";
            PreparedStatement insertar = miConexion.prepareStatement(sql);
            insertar.setString(1, ve.getColor());
            insertar.setInt(2, ve.getIdCliente());
            insertar.setInt(3, ve.getCodMarca());
            insertar.setInt(4, ve.getModelo());
            insertar.setString(5, ve.getPlaca());
            
            insertar.execute();
            JOptionPane.showMessageDialog(null, "Registro Guardado Exitosamente.");
        } catch (SQLException er) {
            System.err.println("No se pudo conectar o hacer insercion. " + er.getMessage());
        }finally{
            conexionBD.setDesconectar();
        }
    }
    
    public void editar (claseVehiculo ve){
        try {
            Connection miConexion = conexionBD.getConnection();
            
            String sql = "UPDATE tbl_vehiculo SET color=?, idCliente=?,codMarca=?,modelo=?  WHERE placa = ?";
            PreparedStatement actualizar = miConexion.prepareStatement(sql);
            actualizar.setString(1, ve.getColor());
            actualizar.setInt(2, ve.getIdCliente());
            actualizar.setInt(3, ve.getCodMarca());
            actualizar.setInt(4, ve.getModelo());
            actualizar.setString(5, ve.getPlaca());
            
            actualizar.executeUpdate();
            JOptionPane.showMessageDialog(null, "Registro Actualizado Exitosamente.");
            
        } catch (SQLException er) {
            System.err.println("No se pudo conectar o hacer Actualizado. " + er.getMessage());
        }finally{
            conexionBD.setDesconectar();
        }
    }
}

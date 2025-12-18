package rnml20230828.accesoadatos;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import rnml20230828.entidades.Empleados;

public class EmpleadosDAL {
    public static ArrayList<Empleados> listarEmpleados() throws Exception {
        ArrayList<Empleados> empleados = new ArrayList<>();
        try (Connection conn = ComunDB.obtenerConexion()) {
            try (Statement statement = conn.createStatement(); ResultSet resultSet = statement.executeQuery("SELECT * FROM Empleados")) {

                while (resultSet.next()) {
                    int Id = resultSet.getInt("Id");
                    String Nombre = resultSet.getString("Nombre");
                    String Apellido = resultSet.getString("Apellido");
                    String Email = resultSet.getString("Email");
                    String PuestoEmpleado = resultSet.getString("PuestoEmpleado");

                    Empleados empleado = new Empleados(Id, Nombre,Apellido, Email, PuestoEmpleado);
                    empleados.add(empleado);
                }
            }
        } catch (SQLException ex) {
            throw ex;
        }
        return empleados;
    }
    
    public static int agregarEmpleados(Empleados Empleados) throws SQLException {
        int result = 0;
        try (Connection conn = ComunDB.obtenerConexion(); PreparedStatement statement = conn.prepareStatement(
                "INSERT INTO Empleados (Nombre,Apellido, Email, PuestoEmpleado) VALUES (?, ?, ?,?)")) {

            statement.setString(1, Empleados.getNombre());
            statement.setString(2, Empleados.getApellido());
            statement.setString(3, Empleados.getEmail());
            statement.setString(4, Empleados.getPuestoEmpleado());

            result = statement.executeUpdate();
        }
        return result;
    }
    
     public static int editarEmpleados(Empleados Empleados) throws SQLException {
        int result = 0;
        try (Connection conn = ComunDB.obtenerConexion(); PreparedStatement statement = conn.prepareStatement(
                "UPDATE Empleados SET Nombre = ?, Apellido = ?, Email = ?, PuestoEmpleado = ? WHERE Id = ?")) {

            statement.setString(1, Empleados.getNombre());
            statement.setString(2, Empleados.getApellido());
            statement.setString(3, Empleados.getEmail());
            statement.setString(4, Empleados.getPuestoEmpleado());
            statement.setInt(5, Empleados.getId());

            result = statement.executeUpdate();
        }
        return result;
    }
      public static Empleados obtenerEmpleadosPorId(int empleadoId) throws Exception {
        Empleados empleado = null;
        try (Connection conn = ComunDB.obtenerConexion()) {
            String query = "SELECT * FROM Empleados WHERE Id = ?";

            try (PreparedStatement preparedStatement = conn.prepareStatement(query)) {
                preparedStatement.setInt(1, empleadoId);
                try (ResultSet resultSet = preparedStatement.executeQuery()) {
                    if (resultSet.next()) {
                       int Id = resultSet.getInt("Id");
                    String Nombre = resultSet.getString("Nombre");
                    String Apellido = resultSet.getString("Apellido");
                    String Email = resultSet.getString("Email");
                    String PuestoEmpleado = resultSet.getString("PuestoEmpleado");

                    empleado = new Empleados(Id, Nombre,Apellido, Email, PuestoEmpleado);
                    }
                }
            }
        } catch (SQLException ex) {
            throw ex;
        }
        return empleado;
    }
}

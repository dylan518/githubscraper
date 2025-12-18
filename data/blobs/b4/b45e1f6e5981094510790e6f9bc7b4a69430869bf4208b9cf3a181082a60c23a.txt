package formularios;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import javax.swing.JOptionPane;


public class Conexion {
    String nombreBD = "autopartes";
    String user = "root";
    String pass = "";
    String URL = "jdbc:mysql://localhost:3306/" + nombreBD;
    String CLASE = "com.mysql.cj.jdbc.Driver";
    Connection con;
    
    public Connection getConnection() {
        try {
            Class.forName(CLASE);
            con = (Connection) DriverManager.getConnection(URL, user, pass);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "No se ha establecido conexion con la base de datos "+nombreBD, "Error", JOptionPane.ERROR_MESSAGE);
        }
        return con;
    }
    
    public void close(){
        try {
            con.close();
        } catch (SQLException e) {
            System.out.println(e);
        }
    }
    
    public static void main(String[] args) {
        Conexion c = new Conexion();
        c.getConnection();
    }
}

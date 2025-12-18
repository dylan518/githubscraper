/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Config;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 *
 * @author Minguel
 */
public class Conexion {
    
     private String USERNAME = "root";
    private String PASSWORD = "root";
    private String HOST = "localhost";
    private String PORT = "3306";
    private String DATABASE = "pa";
    private String CLASSNAME = "com.mysql.cj.jdbc.Driver";
    private String URL = "jdbc:mysql://" + HOST + ":" + PORT + "/" + DATABASE + "?serverTimezone=UTC";

    private Connection con;

    public Conexion() throws SQLException {

        try {
            Class.forName(CLASSNAME);
            con = DriverManager.getConnection(URL, USERNAME, PASSWORD);
        } catch (ClassNotFoundException e) {
            System.err.println("Error 1: " + e);
        } catch (SQLException e) {
            System.err.println("Error 2: " + e);
        }
    }

    public Connection getConexion() {
        return con;  //retornar el objeto que contiene la conexión
    }

    public void close() {
        con = null;
    }

///para verificar la conexión
    public static Connection conn;
    private static Statement stm;
    private static ResultSet rs;

    public static void main(String[] args) throws SQLException {
        Conexion c1 = new Conexion();
        Conexion.conn = c1.getConexion();

        if (conn != null) {
            System.out.println("Conexión exitosa.... ");
            System.out.println("--------------------");
        }

    }

}

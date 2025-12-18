/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Dal;

/**
 *
 * @author Admin
 */
<<<<<<< Updated upstream
public class DBContext {
    
=======
public abstract class DBContext<T> {

    protected Connection connection;

    public DBContext() {
        try {
            String url = "jdbc:sqlserver://localhost:1433;databaseName=HappyPrograming;encrypt=true;trustServerCertificate=true;";
            String user = "sa";
            String pass = "123";
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            connection = DriverManager.getConnection(url, user, pass);
            Logger.getLogger(DBContext.class.getName()).log(Level.INFO, "Connection established successfully.");
        } catch (ClassNotFoundException | SQLException ex) {
            Logger.getLogger(DBContext.class.getName()).log(Level.SEVERE, "Connection failed.", ex);
        }
    }

    public Connection getConnection() {
        return connection;
    }

>>>>>>> Stashed changes
}

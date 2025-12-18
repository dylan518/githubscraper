import java.sql.Connection;
import java.sql.*;
import java.sql.Statement;
import java.sql.DriverManager;
import java.sql.SQLException;

public class student {

    public static void main(String[] args) throws Exception {
        Connection c = null;
        Statement stmt = null;

        try {
            Class.forName("org.postgresql.Driver");
            c = DriverManager.getConnection("jdbc:postgresql://localhost/pg", "postgres", "bca");
            System.out.println("Open database successfully!");
            stmt = c.createStatement();
            String sql = "CREATE TABLE STUDENTS" +
                    "(ID INT PRIMARY KEY NOT NULL," +
                    "NAME TEXT NOT NULL," +
                    "AGE INT NOT NULL)";
            stmt.execute(sql);
            stmt.close();
            c.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ":" + e.getMessage());
            System.exit(0);
        }

        System.out.println("Table created successfully");

    }
}
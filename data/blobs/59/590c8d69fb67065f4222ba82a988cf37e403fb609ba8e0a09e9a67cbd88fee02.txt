package com.goit.feature.db;


import com.goit.feature.preferences.Prefs;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class Database {
    private static final Database INSTANCE = new Database();
    private Connection connection;
    public Database() {
        try {
            String dbUrl = new Prefs().getString(Prefs.DB_JDBC_CONNECTION_URL);
            connection = DriverManager.getConnection(dbUrl);
        } catch (SQLException e){
            e.printStackTrace();
        }
    }
    public static Database getInstance() {
        return INSTANCE;
    }
    public int executeUpdate(String sql){
        try ( Statement statement = connection.createStatement()){
            return statement.executeUpdate(sql);
        } catch (SQLException e) {
            e.printStackTrace();
            return -1;
        }
    }


    public Connection getConnection() {
        return connection;
    }
    public void close(){
        try {
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}

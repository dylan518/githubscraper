package com.banking.javabankingapplication.dbconnection.loginconnection;



import com.banking.javabankingapplication.dbconnection.DatabaseConnector;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.stage.Stage;

import java.io.IOException;
import java.sql.*;

public class LoginDataSender extends DatabaseConnector {


    public boolean authenticateUser(String username, String password) {
        boolean isAuthenticated = false;

        try {
            ensureConnection();
            // Connect to database


            // Prepare statement
            String query = "SELECT * FROM user_authentication WHERE username = ? AND password = ?";
            statement = connection.prepareStatement(query);
            statement.setString(1, username);
            statement.setString(2, password);

            // Execute query
            ResultSet rs = statement.executeQuery();

            // Check if there is a matching user
            if (rs.next()) {
                isAuthenticated = true;
            }

            // Close resources
            rs.close();
            statement.close();
            connection.close();
            disconnect();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return isAuthenticated;
    }




}
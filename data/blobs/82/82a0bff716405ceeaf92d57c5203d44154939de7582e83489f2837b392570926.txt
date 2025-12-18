package com.example.todo;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;
import java.sql.*;
import static com.example.todo.HelloController.setUsername;

public class signupcontroller extends NullPointerException{

    @FXML
    private TextField UUsername;

    @FXML
    private TextField name;

    @FXML
    private TextField password;

    @FXML
    private PasswordField confirmpassword;


    @FXML
    private TextField mobno;

    @FXML
    private TextField email;

    @FXML
    private Label errorusername;

    @FXML
    private Label errorname;

    @FXML
    private Label errorpassword;

    @FXML
    private Label errorconfirmpassword;


    @FXML
    private Label errormobno;

    @FXML
    private Label erroremail;

    public void onSignUpButtonClick(ActionEvent event) throws IOException {
        System.out.println("Button clicked!");
        if ( !UUsername.getText().isBlank() && !name.getText().isBlank() && !password.getText().isBlank()
                && !confirmpassword.getText().isBlank() && !mobno.getText().isBlank() && !email.getText().isBlank() ){
            validateSignUp(event);
        }
        else {

            if(UUsername.getText().isBlank()){
                errorusername.setText("⚠ Please enter username!");
                UUsername.setStyle("-fx-border-color: #00ffff; -fx-border-width: 2px");
            }
            else {
                errorusername.setText(null);
                UUsername.setStyle(null);
            }
            if(name.getText().isBlank()){
                errorname.setText("⚠ Please enter full name!");
                name.setStyle("-fx-border-color: #00ffff; -fx-border-width: 2px");
            }
            else {
                errorname.setText(null);
                name.setStyle(null);
            }
            if(password.getText().isBlank()){
                errorpassword.setText("⚠ Please enter password!");
                password.setStyle("-fx-border-color: #00ffff; -fx-border-width: 2px");
            }
            else {
                errorpassword.setText(null);
                password.setStyle(null);
            }
            if(confirmpassword.getText().isBlank()){
                errorconfirmpassword.setText("⚠ Please enter password!");
                confirmpassword.setStyle("-fx-border-color: #00ffff; -fx-border-width: 2px");
            }
            else {
                errorconfirmpassword.setText(null);
                confirmpassword.setStyle(null);
            }

            if(mobno.getText().isBlank()){
                errormobno.setText("⚠ Please enter your mobile no!");
                mobno.setStyle("-fx-border-color: #00ffff; -fx-border-width: 2px");
            }
            else {
                errormobno.setText(null);
                mobno.setStyle(null);
            }
            if(email.getText().isBlank()){
                erroremail.setText("⚠ Please enter email-id!");
                email.setStyle("-fx-border-color: #00ffff; -fx-border-width: 2px");
            }
            else {
                erroremail.setText(null);
                email.setStyle(null);
            }


        }
    }

    private void validateSignUp(ActionEvent event) {
        System.out.println("Inside function signup");
        DBConnect connectnow = new DBConnect();
        Connection connectdb = connectnow.getConnection();
        String verifySignup = "select count(1) from ontrackdb_1.user_details where username = '" + UUsername.getText() +"' ";
        Statement statement = null;
        /*int i = mobno.getText().length();
        if (i>10 || i<10){
            errorMobNo.setText("⚠ Please enter correct mobile no!");
            mobno.setStyle("-fx-border-color: red; -fx-border-width: 2px; -fx-border-radius: 15px");
        }*/

        try {
            statement = connectdb.createStatement();
            ResultSet queryResult = statement.executeQuery(verifySignup);
            while (queryResult.next()) {
                System.out.println("Inside while loop");
                if (queryResult.getInt(1) == 1) {
                    System.out.println("inside if");
                    UUsername.setStyle("-fx-border-color: #00ffff; -fx-border-width: 2px");
                    errorusername.setText("⚠ This username already exists");
                } else {
                    if (password.getText().equals(confirmpassword.getText())) {
                        System.out.println("inside else");
                        String insertDetails = "INSERT INTO ontrackdb_1.user_details (`username`, `name`, `password`, `mobile_no`,`email_id`) VALUES ('" + UUsername.getText() + "','" + name.getText() + "','" + password.getText() + "','" + mobno.getText() + "','" + email.getText() + "' \n)";

                        try {
                            statement = connectdb.createStatement();
                            int a = statement.executeUpdate(insertDetails);

                            if (a == 1) {
                                System.out.println("Inserted data!");
                            } else {
                                System.out.println("Failed to insert data");
                            }
                            Parent root = FXMLLoader.load(getClass().getResource("home.fxml")); //pass scene name here
                            Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
                            Scene scene = new Scene(root);
                            stage.setScene(scene);
                            stage.show();
                            setUsername(String.valueOf(UUsername));
                        } catch (Exception e) {
                            e.printStackTrace();
                            e.getCause();
                        }
                    }
                    else {
                        errorpassword.setText("These fields");
                        errorconfirmpassword.setText(" should match!");
                    }
                }
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @FXML
    public  void switchTologin(ActionEvent event) throws IOException {

        Parent root = FXMLLoader.load(getClass().getResource("login.fxml"));
        Stage stage = (Stage) ((Node)event.getSource()).getScene().getWindow();
        Scene scene = new Scene(root);
        stage.setScene(scene);
    }


}

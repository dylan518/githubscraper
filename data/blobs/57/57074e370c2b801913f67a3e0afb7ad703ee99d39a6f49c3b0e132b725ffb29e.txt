package de.iav.firstapp;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class StudentController {
    @FXML
    private TextField firstNameField;

    @FXML
    private TextField lastNameField;

    @FXML
    private TextField emailField;

    @FXML
    private TextField courseField;

    @FXML
    private CheckBox gdprCheckbox;

    @FXML
    private Button registerButton;


    private Stage stage;
    private Scene scene;
    private Parent root;

    @FXML
    protected void onHelloButtonClick(ActionEvent printEvent) throws IOException {

        String firstName = firstNameField.getText();
        String lastName = lastNameField.getText();
        String email = emailField.getText();
        String courseOfStudies = courseField.getText();

        Student student = new Student(firstName, lastName, email, courseOfStudies);
        FXMLLoader loader = new FXMLLoader(getClass().getResource("Registered_Students.fxml"));
        root = loader.load();

        RegisteredStudentsController registeredStudentsController= loader.getController();
        stage = (Stage) ((Node) printEvent.getSource()).getScene().getWindow();
        registeredStudentsController.addStudentToList(student);

        scene = new Scene(root);
        stage.setScene(scene);

        stage.show();
        }

        @FXML
        public void switchBackToGreetings(ActionEvent backEvent) throws IOException {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("welcome.fxml"));
            root = loader.load();

            GreetingsController scene1Controller = loader.getController();

            stage = (Stage) ((Node) backEvent.getSource()).getScene().getWindow();
            scene = new Scene(root);
            stage.setScene(scene);

            stage.show();
        }

        //I
        public void initialize() {
            registerButton.setDisable(true);
        }
        @FXML
        public void isGdprBoxChecked() {
            if (gdprCheckbox.isSelected()) {
                registerButton.setDisable(false);
            } else {
                registerButton.setDisable(true);
            }
        }

    }
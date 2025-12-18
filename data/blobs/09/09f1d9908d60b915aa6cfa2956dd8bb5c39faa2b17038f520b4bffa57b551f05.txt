package com.example.javafx_demo;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class HelloController {
    @FXML
    private Label welcomeText;

    @FXML
    private TextField text1;

    @FXML
    private TextField text2;

    @FXML
    protected void onHelloButtonClick() {
        String s1,s2;
        s1 = text1.getText();
        s2 = text2.getText();
        int a1=Integer.parseInt(s1);
        int a2=Integer.parseInt(s2);
        welcomeText.setText(Integer.toString(a1+a2));
    }
}
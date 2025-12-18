/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package edu.ijse.crs.view;

import edu.ijse.crs.service.StudentService;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

/**
 *
 * @author Asus
 */
public class StudentView extends JFrame {
    private JTextField nameField, dobField, programField, yearField;
    private JButton addButton;
    private StudentService studentService;

    public StudentView() {
        studentService = new StudentService();
        setTitle("Student Management");
        setSize(400, 300);
        setLayout(new GridLayout(5, 2));
        
        add(new JLabel("Name:"));
        nameField = new JTextField();
        add(nameField);
        
        add(new JLabel("Date of Birth:"));
        dobField = new JTextField();
        add(dobField);
        
        add(new JLabel("Program:"));
        programField = new JTextField();
        add(programField);
        
        add(new JLabel("Year:"));
        yearField = new JTextField();
        add(yearField);
        
        addButton = new JButton("Add Student");
        addButton.addActionListener(e -> {
            studentService.registerStudent(nameField.getText(), dobField.getText(), programField.getText(), Integer.parseInt(yearField.getText()));
            JOptionPane.showMessageDialog(this, "Student Added Successfully");
        });
        add(addButton);
    }
}
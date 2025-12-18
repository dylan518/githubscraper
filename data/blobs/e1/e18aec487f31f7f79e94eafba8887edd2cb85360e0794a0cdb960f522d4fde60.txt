/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package edad;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

/**
 *
 * @author besker
 */
public class Edad extends JFrame implements ActionListener {

    JPanel panel01;
    JTextField txtEdad;
    JButton b1;
    private int edad;
    private String res;

    public Edad() {
        this.setSize(30, 90);
        this.setTitle("Programa edad");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        txtEdad = new JTextField(10);
// add (txtEdad);
        panel01 = new JPanel(new GridLayout(2, 1));
        b1 = new JButton("Dame tu edad");
        panel01.add(txtEdad); //6+ OnclickListener(this);
        panel01.add(b1);
        add(panel01);
        b1.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e) {

        int edad = Integer.parseInt(txtEdad.getText());
        String res = " ";

        if (edad >= 18) {
            res = "Mayor de Edad";
            System.out.println("Mayor de Edad");
        } else {
            res = "Menor de edad";
            System.out.println("Menor de edad");
        }
        JOptionPane.showMessageDialog(null, res);
        
    }
}

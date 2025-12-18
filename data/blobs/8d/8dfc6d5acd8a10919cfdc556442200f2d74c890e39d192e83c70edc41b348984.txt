/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.cbtlpr2_trabalhofinal;

import java.awt.Color;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;

/**
 *
 * @author  Atilio Almeida Costa
 *          João Victor Crivoi Cesar Souza 
 */
public class ValidadorDeCampos {
    
   
    public static void addValidator(JTextField campo, String tipo){
        campo.getDocument().addDocumentListener(new DocumentListener() {
            @Override
            public void insertUpdate(DocumentEvent e) {
                validar();
            }

            @Override
            public void removeUpdate(DocumentEvent e) {
                validar();
            }

            @Override
            public void changedUpdate(DocumentEvent e) {
                validar();
            }
            private void validar() {
                String texto = campo.getText();
                switch (tipo) {
                    case "idade":
                        if (!texto.matches("\\d*") || !texto.isEmpty() && Integer.parseInt(texto) >= 170) {
                            campo.setBackground(Color.PINK);
                            
                        } else {
                            campo.setBackground(Color.WHITE);
                            
                        }
                        break;
                    case "peso":
                        if (!texto.matches("\\d*\\.?\\d*") || !texto.isEmpty() && Double.parseDouble(texto) >= 500) {
                            campo.setBackground(Color.PINK);
                          
                        } else {
                            campo.setBackground(Color.WHITE);
                            
                            
                        }
                        break;
                    case "altura":
                        if (!texto.matches("\\d*\\.?\\d*")) {
                            campo.setBackground(Color.PINK);
                           
                        } else {
                            campo.setBackground(Color.WHITE);
                            
                        }
                        break;
                }
                
                
            }
        });
    }
    
      public static boolean isAllFieldsFilled(JTextField ... campos){
        for (JTextField campo : campos) {
            if (campo.getText().trim().isEmpty()) {
                return false; 
            }
        }
        return true; 
    }
      
    public static boolean isAllFieldsCorrect(JTextField ... campos){
         for (JTextField campo : campos) {
            if (campo.getBackground().equals(Color.PINK)) {
                return false; 
            }
        }
        return true;
    }
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package GUI;

import compAndDecomp.compressor;
import compAndDecomp.decompressor;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.Color;
import java.io.File;
import java.io.IOException;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

/**
 *
 * @author shubhankar nikam
 */
public class AppFrame extends JFrame implements ActionListener {
    
    //created two button one for copression and second for the decrompresson.
    JButton compressButton;
    JButton decompressButton;
    
    //constuctor of 'AppFrame'
    AppFrame()
    {
        //below line used when we close window.
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        //initilze the 'JButton'
        compressButton = new JButton("select file to compress");
        //set boudn to given button.
        compressButton.setBounds(20, 100, 200, 30);
        
        //adding the action listener to 'compressButton' to 'getSources()'.
        compressButton.addActionListener(this);
        
        //initialize the second 'JButton'
        decompressButton = new JButton("select file to de compress");
        //set bounds to the given buttonn.
        decompressButton.setBounds(20, 100, 200, 30);
        
         //adding the action listener to 'decompressButton' to 'getSources()'.
        decompressButton.addActionListener(this);
        
        //now we addded this button to the frame.
        this.add(compressButton);
        this.add(decompressButton);
        
        //now we set size.
        this.setSize(100, 500);
        
        //now we set the backgraound color.
        this.getContentPane().setBackground(Color.green);
        
        //we set visibility.
        this.setVisible(true);
        
        
    }
    
    //we just overrid the ActionListener to perform action 
    @Override
    public void actionPerformed(ActionEvent e)
    {
        //when we choose the `compressButton`
        if((e.getSource() == compressButton))
        {
            //then we pop window of choose the req. file.
            JFileChooser filechooser = new JFileChooser();
            
            //to see the 'save' button.
            int response = filechooser.showSaveDialog(null);
            
            //if we click on the compress  button. then
            if(response ==  JFileChooser.APPROVE_OPTION)
            {
                //we get the abosoute path of file.
                File file = new File(filechooser.getSelectedFile().getAbsolutePath());
                
                //print
                System.out.println(file);
                
                
                //using try and catch we handle the exception.
                try
                {
                    //going to class copressor and calling method and pass file as a parameter.
                    compressor.method(file);
                }
                catch(IOException p)
                {
                    JOptionPane.showMessageDialog(null, p.toString());
                }
            }
            
        }
        
        //when we choose the `compressButton`
        if((e.getSource() == decompressButton))
        {
            //then we pop window of choose the req. file.
            JFileChooser filechooser = new JFileChooser();
            
            //to see the 'save' button.
            int response = filechooser.showSaveDialog(null);
            
            //if we click on the compress  button. then
            if(response ==  JFileChooser.APPROVE_OPTION)
            {
                //we get the abosoute path of file.
                File file = new File(filechooser.getSelectedFile().getAbsolutePath());
                
                //print
                System.out.println(file);
                
                
                //using try and catch we handle the exception.
                try
                {
                    //going to class copressor and calling method and pass file as a parameter.
                    decompressor.method(file);
                }
                catch(IOException p)
                {
                    JOptionPane.showMessageDialog(null, p.toString());
                }
            }
            
        }
        
        
    }
    
    
}

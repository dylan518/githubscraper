package Frames;

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class admin_panel extends JFrame{
    JLabel text, text1,text3;

	JButton text2;
 
	JButton viewButton,logoutButton;
    JPanel panel;
    Color myColor;
    Font myFont1,myFont2,myFont3;
    Cursor c1;
    ImageIcon img1,img2;
   
    public admin_panel(){
        super("Admin panel");
        this.setSize(850, 600);
	    this.setLocation(500,250);
       
        myColor =new Color(5, 5, 5);
        myFont1 = new Font("Cambria", Font.PLAIN, 40);
        myFont2 = new Font("Cambria", Font.PLAIN, 25);
        myFont3 =new Font("Cambria", Font.PLAIN, 20);
        
        panel = new JPanel();
        panel.setLayout(null);
        panel.setBackground(myColor);

        text1 =new JLabel("Admin Panel");
        text1.setBounds(300,40,300,40);
        text1.setBackground(myColor);
        text1.setForeground(Color.GREEN);
        text1.setOpaque(true);
        text1.setFont(myFont1);
        panel.add(text1);

        text2 = new JButton("Employee Data");
        text2.setBounds(230, 370, 200, 30);
        text2.setBackground(Color.BLUE);
        text2.setForeground(Color.WHITE);
        text2.setFont(myFont3);
        text2.setCursor(c1);
        text2.setBorder(BorderFactory.createEmptyBorder(4, 4, 4, 4));
        text2.setContentAreaFilled(false);
		panel.add(text2);

        

        c1=new Cursor(Cursor.HAND_CURSOR);
        
        

        logoutButton=new JButton("Log out");
        logoutButton.setCursor(c1);
        logoutButton.setBounds(650, 50, 80, 25);
        logoutButton.setBackground(Color.RED);
        logoutButton.setForeground(Color.WHITE);
        logoutButton.setOpaque(true);
        panel.add(logoutButton);
        this.add(panel);
        
        
        logoutButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae) {
                
                    setVisible(false);
                    Started f1 = new Started();
                    f1.setVisible(true);
                
            }
        });
        
        text2.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent ae) {
                
                    setVisible(false);
                    Employee f1 = new Employee();
                    f1.setVisible(true);
                
            }
        });
    }



	



}
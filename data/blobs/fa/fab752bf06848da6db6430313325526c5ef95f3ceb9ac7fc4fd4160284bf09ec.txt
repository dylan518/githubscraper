package quiz.application;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Score extends JFrame implements ActionListener{
    
    JButton submit,back;
    
    Score(String name,int score){
        setBounds(0,0,1370,700);
        getContentPane().setBackground(Color.YELLOW);
        setLayout(null);
        
        ImageIcon i1 = new ImageIcon(ClassLoader.getSystemResource("icons/score.jpg"));
        Image i2 = i1.getImage().getScaledInstance(600, 500, Image.SCALE_DEFAULT);
        ImageIcon i3 = new ImageIcon(i2);
        JLabel image = new JLabel(i3);
        image.setBounds(30,50,600,500);
        add(image);
        
        JLabel heading = new JLabel("Hey...... " + name + "!!!!");
        heading.setBounds(800,100,1400,60);
        heading.setFont(new Font("viner hand itc", Font.PLAIN, 50));
        add(heading);
        
         JLabel heading2 = new JLabel( "Thankyou For Playing Quiz");
        heading2.setBounds(700,200,1400,60);
        heading2.setFont(new Font("cooper black", Font.PLAIN, 40));
        add(heading2);
        
        JLabel lblscore = new JLabel("Your score is " + score);
        lblscore.setBounds(850, 300, 300, 30);
        lblscore.setFont(new Font("Tahoma", Font.BOLD, 36));
        add(lblscore);
        
      /*  submit = new JButton("Play Again");
        submit.setBounds(750, 400, 200, 50);
        submit.setFont(new Font("Times New Roman", Font.BOLD, 25));
        submit.setBackground(new Color(30, 144, 255));
        submit.setForeground(Color.WHITE);
        submit.addActionListener(this);
        add(submit);*/
        
        back =new JButton("Exit");
        back.setBounds(900,400,200,50);
        back.setBackground(new Color(30,144,255));
        back.setFont(new Font("Times New Roman",Font.BOLD,25));
        back.setForeground(Color.WHITE);
        back.addActionListener(this);
        add(back);
        
        setVisible(true);
    }
    
   /* public void actionPerformed(ActionEvent ae){
        setVisible(false);
        new Login();
    }*/
    public void actionPerformed(ActionEvent ae) {
       /* if(ae.getSource() == submit){
            setVisible(false);
            new Login();
            dispose();
        }else*/ if (ae.getSource() == back){
              setVisible(false);
        }
    }
    
     public static void main(String args[]){
        new Score("User",0);
     
    }
}

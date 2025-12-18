package layoutmanager3;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class LayoutManager3 implements ActionListener{
    JFrame jfrm;
    JLabel jlab1, jlab2;
    JTextField tf1, tf2;
    JButton jbtn1, jbtn2;
    JLabel jlab;
    LayoutManager3(){
        jfrm = new JFrame("Content Pane");
        jfrm.setLayout(new BorderLayout());
        jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jfrm.setSize(300, 300);
        
        Font fon = new Font("Arial", Font.BOLD,30);
        
        JPanel jp = new JPanel();
        JPanel jp2 = new JPanel();
        JPanel jp3 = new JPanel();
        JPanel jp4 = new JPanel();
        JPanel jpmain = new JPanel(new BorderLayout());
        jlab1 = new JLabel("INSERT 1st no");
        tf1 = new JTextField("9", 10);
        jlab2 = new JLabel("INSERT 2st no");
        tf2 = new JTextField("2", 10);
       
        jbtn1 = new JButton("calc");
        jbtn2 = new JButton("clear");
        
        jlab = new JLabel();
        jlab.setFont(fon);
        
        jp.add(jlab1);
        jp.add(tf1);
        jp2.add(jlab2);
        jp2.add(tf2);
        jp3.add(jbtn1);
        jp3.add(jbtn2);
        jp4.add(jlab);
        jp4.add(jlab);

        jpmain.add(jp, BorderLayout.NORTH);
        jpmain.add(jp2, BorderLayout.CENTER);
        jpmain.add(jp3, BorderLayout.SOUTH);
                
        jbtn1.addActionListener(this);
        jbtn2.addActionListener(this);
//        tf1.addActionListener(this);
//        tf2.addActionListener(this);
        
        
        jfrm.add(jpmain,BorderLayout.NORTH);
//        jfrm.add(jp, BorderLayout.NORTH);
//        jfrm.add(jp2);
//        jfrm.add(jp3);
        jfrm.add(jp4, BorderLayout.CENTER);
        
        jfrm.setVisible(true);
    }
    
    public void actionPerformed(ActionEvent ae){
        if(ae.getSource() == jbtn1){
        double x = Double.parseDouble(tf1.getText());
        double y = Double.parseDouble(tf2.getText());
        double result = x/y;
        jlab.setText("answer= " + result);
        }
        else if (ae.getSource() == jbtn2){
            tf1.setText("");
            tf2.setText("");
            jlab.setText("");
        }
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            
            @Override
            public void run() {
                new LayoutManager3();
            }
        });
    }
}

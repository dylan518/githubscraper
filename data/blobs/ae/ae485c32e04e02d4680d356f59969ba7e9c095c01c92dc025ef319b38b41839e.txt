package Nine;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;

import javax.swing.*;

public class Seven extends JFrame{
	public Seven() {
		setTitle("pra");
		setSize(300,300);
		Container c=getContentPane();
		c.setLayout(new BorderLayout());
		c.add(new panel_north(),BorderLayout.NORTH);
		c.add(new panel_center(),BorderLayout.CENTER);
		c.add(new panel_south(),BorderLayout.SOUTH);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public static void main(String[] args) {
		new Seven();
	}
}

class panel_north extends JPanel{
	public panel_north() {
		setLayout(new FlowLayout());
		setBackground(Color.GRAY);
		add(new JLabel("수식입력"));
		add(new JTextField(10));
		setVisible(true);
	}
}

class panel_center extends JPanel{
	JButton []b=new JButton[10];
	public panel_center() {
		setLayout(new GridLayout(4,4,5,5));
		for(int i=0;i<b.length;i++) {
			b[i]=new JButton(Integer.toString(i));
			add(b[i]);
		}
		add(new JButton("CE"));
		add(new JButton("계산"));
		add(new JButton("+")).setBackground(Color.CYAN);
		add(new JButton("-")).setBackground(Color.CYAN);
		add(new JButton("x")).setBackground(Color.CYAN);
		add(new JButton("/")).setBackground(Color.CYAN);
	}
}

class panel_south extends JPanel{
	public panel_south() {
		setLayout(new FlowLayout());
		setBackground(Color.YELLOW);
		add(new JLabel("계산 결과"));
		add(new JTextField(10));
		setVisible(true);
	}
}
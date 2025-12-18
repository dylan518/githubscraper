package basics;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;

public class DemoJList extends JFrame {
	
	public DemoJList() {
		this.setVisible(true);
		this.setTitle("Jlist Demo");
		this.setLayout(null);
		
		JLabel jLabel = new JLabel("List");
		jLabel.setSize(400,100);
		
		JButton jButton = new JButton("Click");
		jButton.setBounds(40,80,60,30);
		
		DefaultListModel<String> lm = new DefaultListModel<String>();
		lm.addElement("Java");
		lm.addElement("Spring");
		lm.addElement("Hibernate");
		lm.addElement("Springboot");
		
		JList<String> l = new JList<String>(lm);
		l.setBounds(100, 150, 70, 75);
		
		this.add(l);
		this.add(jButton);
		this.add(jLabel);
		
		this.setSize(500,500);
	}
	
	public static void main(String[] args) {
		new DemoJList();
	}
}

import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class JcheckboxProgram extends JFrame
{
	static JFrame f;

	public static void main(String args[])
	{
		f = new JFrame("checkbox");
		JCheckBox c1 = new JCheckBox("CheckBox1");
		JCheckBox c2 = new JCheckBox("CheckBox2");
		f.setLayout(new FlowLayout());
		JPanel p = new JPanel();

		p.add(c1);
		p.add(c2);

		f.add(p);
		f.setSize(300,300);
		f.show();
	}
}
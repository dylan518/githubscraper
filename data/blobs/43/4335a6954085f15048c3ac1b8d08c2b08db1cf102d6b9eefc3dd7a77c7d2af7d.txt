import java.awt.Point;
import java.awt.Toolkit;

import javax.swing.JFrame;

public class portatil {
	public static void main(String[] args) {
		Window window = new Window();
	}
}

public class Window {
	JFrame frame;
	
	public Window() {
		frame = new JFrame();
		frame.setTitle("Cachipun");
		frame.setSize(500, 500);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setResizable(false);
		frame.setLocation(300, Toolkit.getDefaultToolkit().getScreenSize().height - 400);
		frame.setVisible(true);
	}
}

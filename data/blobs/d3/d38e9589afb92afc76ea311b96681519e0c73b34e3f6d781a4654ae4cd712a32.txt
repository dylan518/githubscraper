package ppt.ppt08;
import java.awt.*;
import javax.swing.*;

public class MyFrame2 extends JFrame {
	public MyFrame2() {
		setSize(300, 150);			// (1) JFrame의 크기를 설정한다. 
		setLocation(200, 300);		// (2) JFrame의 위치를 설정한다. 
		setTitle("MyFrame");
		setLayout(new FlowLayout());
		getContentPane().setBackground(Color.yellow);		// (3) 배경색을 변경한다.
		JButton button1 = new JButton("확인");
		JButton button2 = new JButton("취소");
		this.add(button1);
		this.add(button2);
		setVisible(true);
	}
    public static void main(String[] args) {
        MyFrame f = new MyFrame();
  }
}
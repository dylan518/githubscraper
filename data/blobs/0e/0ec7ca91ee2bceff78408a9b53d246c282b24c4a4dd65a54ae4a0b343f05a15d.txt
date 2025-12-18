package c_sample;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;


/*
 *  화면(JFrame)에 '확인' 버튼 하나 출력
 */

public class EventTest {
	JFrame f;
	JButton bt;

	EventTest() {
		
		f = new JFrame();
		bt = new JButton("확인");
		
		//(2)핸들러 객체 생성
		MYHandler hdlr = new MYHandler();
		
		bt.addActionListener(hdlr);
		
	}

	// (1)이벤트 핸들러 만들기
	// 핸들러 - 이벤트 처리 클래스
	class MYHandler implements ActionListener {
		public void actionPerformed(ActionEvent e) {

			JOptionPane.showMessageDialog(null, "이벤트발생");
		}
	}

	public void addLayout() {
		f.add(bt);

		f.setBounds(100, 100, 500, 200);
		f.setVisible(true);
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {

		EventTest info = new EventTest();
		info.addLayout();
	}

}


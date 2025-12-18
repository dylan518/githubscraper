package classi;

import java.awt.CardLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Container extends JFrame{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	static mainmenu primoframe;
	static helpframe secondoframe;
	static gamepanel terzoframe;
	static loseframe quartoframe;
	static gamecore gc;
	
	static JPanel contentPane;
	
	public Container() {
		super("Brick Breaker");

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(800, 600);
		setVisible(true);
		setResizable(false);
		
		contentPane = new JPanel();
		setContentPane(contentPane);
		contentPane.setLayout(new CardLayout(0, 0));
		primoframe = new mainmenu();
		contentPane.add(primoframe);
		
		secondoframe = new helpframe(this);
		contentPane.add(secondoframe);
		
		gc = new gamecore();
		terzoframe = new gamepanel(gc, this);
		contentPane.add(terzoframe);
		
		quartoframe = new loseframe(primoframe, this);
		contentPane.add(quartoframe);
		
		primoframe.sethelp(secondoframe);
		primoframe.setgame(terzoframe);
		secondoframe.setmain(primoframe);
		terzoframe.setmain(primoframe);
		terzoframe.setlose(quartoframe);
	}
		
	public void setcore() {gc = new gamecore();
	terzoframe.resetgamepanel(gc);
	}
	public int getscore() {
		return gc.getScore();
	}
	public int getlives() {
		return gc.getLives();
	}
	public int getlvl() {
		return gc.getLVL();
	}
	public void setlives(int i) {
		gc.modlives(i);
	}

	
public static void main(String[] args) {

	EventQueue.invokeLater(new Runnable() {
		public void run() {
			try {
				Container frame = new Container();
				frame.setVisible(true);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	});
}


}
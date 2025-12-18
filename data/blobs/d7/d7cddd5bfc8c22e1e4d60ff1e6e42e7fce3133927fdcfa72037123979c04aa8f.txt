package gui;

import javax.swing.JFrame;
import javax.swing.JPanel;

import schedule.Schedule;
import schedule.ScheduleManager;


public class WindowFrame extends JFrame{
	
	ScheduleManager scheduleManager;
	ScheduleAdder scheduleadder; 
	ScheduleViewer scheduleViewer;
	MenuSelection menuselection;

	public WindowFrame(ScheduleManager scheduleManager) {

		this.scheduleManager = scheduleManager;
		this.scheduleadder = new ScheduleAdder(this); 
		this.scheduleViewer = new ScheduleViewer(this, this.scheduleManager);
		this.menuselection = new MenuSelection(this);

		
		this.setSize(500, 300);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		this.setupPanel(menuselection);
		
		this.setVisible(true);
	}
	
	
	public void setupPanel(JPanel panel) {
		this.getContentPane().removeAll();
		this.getContentPane().add(panel);
		this.revalidate();
		this.repaint();
	}
	

	public ScheduleAdder getScheduleadder() {
		return scheduleadder;
	}


	public void setScheduleadder(ScheduleAdder scheduleadder) {
		this.scheduleadder = scheduleadder;
	}


	public ScheduleViewer getScheduleViewer() {
		return scheduleViewer;
	}


	public void setScheduleViewer(ScheduleViewer scheduleViewer) {
		this.scheduleViewer = scheduleViewer;
	}


	public MenuSelection getMenuselection() {
		return menuselection;
	}


	public void setMenuselection(MenuSelection menuselection) {
		this.menuselection = menuselection;
	}

}

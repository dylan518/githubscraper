package screens;

import java.lang.ModuleLayer.Controller;

import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.SwingConstants;

import controller.MainController;

import java.awt.Font;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.Color;
import javax.swing.UIManager;

public class MainScreen extends JPanel {

	private static final long serialVersionUID = 1L;
	private MainController controller;
	/**
	 * Create the panel.
	 */
	public MainScreen(MainController controller) {
		this.controller = controller;
		setLayout(null);
		
		JLabel lblWelcome = new JLabel("Welcome");
		lblWelcome.setFont(new Font("Verdana", Font.BOLD, 20));
		lblWelcome.setHorizontalAlignment(SwingConstants.CENTER);
		lblWelcome.setBounds(114, 38, 198, 41);
		add(lblWelcome);
		
		JButton btnLogIn = new JButton("Log In");

		btnLogIn.setBackground(UIManager.getColor("Button.light"));

		btnLogIn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				controller.goToLogInScreen();
				
			}
		});
		btnLogIn.setBounds(171, 102, 89, 23);
		add(btnLogIn);
		
		JButton btnSignUp = new JButton("Sign up");
		btnSignUp.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				controller.goToSignUpScreen();
			}
		});
		btnSignUp.setBounds(171, 136, 89, 23);
		add(btnSignUp);
		

	}
	
}

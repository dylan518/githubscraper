package View;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.ImageIcon;
import java.awt.SystemColor;
import java.awt.Color;
import java.awt.Toolkit;

public class Register extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Register frame = new Register();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Register() {
		setIconImage(Toolkit.getDefaultToolkit().getImage("D:\\User\\Documents\\WhatsApp Image 2023-01-01 at 11.58.09.jpeg"));
		setTitle("REGISTER");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 652, 472);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(204, 102, 102));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btnPatient = new JButton("");
		btnPatient.setIcon(new ImageIcon("D:\\User\\Documents\\patient baru.png"));
		btnPatient.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				PatientRegister frame = new PatientRegister();
				frame.setVisible(true);
				dispose();
			}
		});
		btnPatient.setFont(new Font("Tahoma", Font.PLAIN, 16));
		btnPatient.setBounds(421, 154, 161, 138);
		contentPane.add(btnPatient);
		
		JButton btnBack = new JButton("BACK");
		btnBack.setForeground(Color.BLACK);
		btnBack.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				MainMenu frame = new MainMenu();
				frame.setVisible(true);
				dispose();
			}
		});
		btnBack.setFont(new Font("Cambria", Font.PLAIN, 18));
		btnBack.setBounds(465, 387, 161, 35);
		contentPane.add(btnBack);
		
		JButton btnPatient_1 = new JButton("");
		btnPatient_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				NurseRegister frame = new NurseRegister();
				frame.setVisible(true);
				dispose();
			}
		});
		btnPatient_1.setIcon(new ImageIcon("D:\\User\\Documents\\nurse baru.png"));
		btnPatient_1.setFont(new Font("Tahoma", Font.PLAIN, 16));
		btnPatient_1.setBounds(229, 154, 161, 138);
		contentPane.add(btnPatient_1);
		
		JButton btnPatient_2 = new JButton("");
		btnPatient_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				DoctorRegister frame = new DoctorRegister();
				frame.setVisible(true);
				dispose();
			}
		});
		btnPatient_2.setIcon(new ImageIcon("D:\\User\\Documents\\doctor baru.png"));
		btnPatient_2.setFont(new Font("Tahoma", Font.PLAIN, 16));
		btnPatient_2.setBounds(43, 154, 161, 138);
		contentPane.add(btnPatient_2);
		
		JLabel lblRegisterPage = new JLabel("REGISTER PAGE");
		lblRegisterPage.setForeground(Color.BLACK);
		lblRegisterPage.setFont(new Font("Cambria", Font.BOLD, 25));
		lblRegisterPage.setBounds(215, 70, 196, 29);
		contentPane.add(lblRegisterPage);
		
		JLabel lblNewLabel = new JLabel("DOCTOR");
		lblNewLabel.setForeground(Color.BLACK);
		lblNewLabel.setFont(new Font("Cambria", Font.BOLD, 18));
		lblNewLabel.setBounds(89, 303, 78, 29);
		contentPane.add(lblNewLabel);
		
		JLabel lblNurse = new JLabel("NURSE");
		lblNurse.setForeground(Color.BLACK);
		lblNurse.setFont(new Font("Cambria", Font.BOLD, 18));
		lblNurse.setBounds(283, 303, 63, 29);
		contentPane.add(lblNurse);
		
		JLabel lblPatient = new JLabel("PATIENT");
		lblPatient.setForeground(Color.BLACK);
		lblPatient.setFont(new Font("Cambria", Font.BOLD, 18));
		lblPatient.setBounds(465, 303, 78, 29);
		contentPane.add(lblPatient);
	}
}

package demo;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import javax.swing.border.EmptyBorder;

public class Frame1 extends JFrame {

	static final String DB_URL = "jdbc:mysql://localhost/dbms_miniproject";
	static final String USER = "root";
	static final String PASS = "root123";
	Connection conn = null;
	Statement stmt = null;

	private JPanel contentPane;
	private JTextField Name;
	private JTextField Ph_No;
	private JTextField address;
	private JTextField email;
	private JTextField username;
	private JTextField password;
	private JLabel lblNewLabel_6;
	private JButton btnNewButton;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Frame1 frame = new Frame1();
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
	public Frame1() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 919, 614);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(176, 224, 230));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lblNewLabel = new JLabel("NAME");
		lblNewLabel.setFont(new Font("Georgia", Font.BOLD | Font.ITALIC, 16));
		lblNewLabel.setBounds(157, 151, 95, 13);
		contentPane.add(lblNewLabel);

		JLabel lblNewLabel_1 = new JLabel("PHONE NUMBER");
		lblNewLabel_1.setFont(new Font("Georgia", Font.BOLD | Font.ITALIC, 16));
		lblNewLabel_1.setBounds(157, 188, 170, 13);
		contentPane.add(lblNewLabel_1);

		JLabel lblNewLabel_2 = new JLabel("ADDRESS");
		lblNewLabel_2.setFont(new Font("Georgia", Font.BOLD | Font.ITALIC, 16));
		lblNewLabel_2.setBounds(157, 224, 95, 13);
		contentPane.add(lblNewLabel_2);

		JLabel lblNewLabel_3 = new JLabel("EMAIL");
		lblNewLabel_3.setFont(new Font("Georgia", Font.BOLD | Font.ITALIC, 16));
		lblNewLabel_3.setBounds(157, 265, 95, 13);
		contentPane.add(lblNewLabel_3);

		JLabel lblNewLabel_4 = new JLabel("USERNAME");
		lblNewLabel_4.setFont(new Font("Georgia", Font.BOLD | Font.ITALIC, 16));
		lblNewLabel_4.setBounds(157, 314, 120, 13);
		contentPane.add(lblNewLabel_4);

		JLabel lblNewLabel_5 = new JLabel("PASSWORD");
	
		lblNewLabel_5.setFont(new Font("Georgia", Font.BOLD | Font.ITALIC, 16));
		lblNewLabel_5.setBounds(157, 354, 95, 13);
		contentPane.add(lblNewLabel_5);

		Name = new JTextField();
		Name.setBounds(373, 144, 474, 32);
		contentPane.add(Name);
		Name.setColumns(10);

		Ph_No = new JTextField();
		Ph_No.setBounds(373, 181, 474, 32);
		contentPane.add(Ph_No);
		Ph_No.setColumns(10);

		address = new JTextField();
		address.setBounds(373, 223, 474, 32);
		contentPane.add(address);
		address.setColumns(10);

		email = new JTextField();
		email.setBounds(373, 260, 474, 32);
		contentPane.add(email);
		email.setColumns(10);

		username = new JTextField();
		username.setBounds(373, 306, 474, 32);
		contentPane.add(username);
		username.setColumns(10);

		password = new JTextField();
		password.setBounds(373, 349, 474, 32);
		contentPane.add(password);
		password.setColumns(10);

		lblNewLabel_6 = new JLabel("        NEW USER REGISTRATION");
		lblNewLabel_6.setBackground(new Color(128, 128, 255));
		lblNewLabel_6.setFont(new Font("Tahoma", Font.BOLD, 20));
		lblNewLabel_6.setBounds(298, 34, 347, 67);
		contentPane.add(lblNewLabel_6);

		JButton btnNewButton = new JButton("SUBMIT");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String nName, nPh_No, naddress, nemail, nusername;
				int npassword;

				nName = Name.getText();
				nPh_No = Ph_No.getText();
				naddress = address.getText();
				nemail = email.getText();
				nusername = username.getText();
				npassword = Integer.parseInt(password.getText());

				try {
					// to check if the driver is working and the user name and password match;
					// if not, throw exception
					Class.forName("com.mysql.cj.jdbc.Driver");
					System.out.println("connecting to the database");
					conn = DriverManager.getConnection(DB_URL, USER, PASS);
					stmt = conn.createStatement();

					String query = " insert into customer(Name, Phone_No,email,address,password,username)"
							+ " values(?,?,?,?,?,?) ";

					PreparedStatement prep_stmt;

					prep_stmt = conn.prepareStatement(query);
					prep_stmt.setString(1, nName);
					prep_stmt.setString(2, nPh_No);
					prep_stmt.setString(3, nemail);
					prep_stmt.setString(4, naddress);
					prep_stmt.setInt(5, npassword);
					prep_stmt.setString(6, nusername);
					prep_stmt.execute();

					conn.close();

				} catch (Exception x) {
					System.out.println(x);
				}
				Login lg=new Login();
				
				lg.setVisible(true);
				
				


			}
		});
		btnNewButton.setBackground(new Color(0, 128, 64));
		btnNewButton.setForeground(new Color(0, 0, 255));
		btnNewButton.setFont(new Font("Century Gothic", Font.BOLD, 18));
		btnNewButton.setBounds(421, 472, 100, 31);
		contentPane.add(btnNewButton);
	}
}

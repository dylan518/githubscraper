package Vistas;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import java.awt.Color;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.ActionEvent;

public class EventMousePos extends JFrame implements ActionListener, MouseListener{

	private JPanel contentPane;
	private JLabel lblNombre;
	private JButton btnEsquina;
	private JButton btnCentro;
	private JButton btnAgrandar;
	private JButton btnAchicar;

	public EventMousePos() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(760, 458);
		setLocationRelativeTo(null);
		iniciar();
	}

	public void iniciar() {
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		 lblNombre = new JLabel("Juan Jos\u00E9 Ca\u00F1as");
		lblNombre.setBackground(Color.GREEN);
		lblNombre.setOpaque(true);
		lblNombre.setHorizontalAlignment(SwingConstants.CENTER);
		lblNombre.setBounds(270, 65, 160, 25);
		contentPane.add(lblNombre);
		
		 btnEsquina = new JButton("Esquina");
		btnEsquina.setBounds(567, 88, 89, 23);
		btnEsquina.addActionListener(this);
		btnEsquina.addMouseListener(this);
		contentPane.add(btnEsquina);
		
		 btnCentro = new JButton("Centro");
		btnCentro.addMouseListener(this);
		btnCentro.addActionListener(this);
		btnCentro.setBounds(567, 139, 89, 23);
		contentPane.add(btnCentro);
		
		 btnAgrandar = new JButton("Agrandar");
		btnAgrandar.setBounds(567, 194, 89, 23);
		btnAgrandar.addMouseListener(this);
		btnAgrandar.addActionListener(this);
		contentPane.add(btnAgrandar);
		
		btnAchicar = new JButton("Achicar");
		btnAchicar.addMouseListener(this);
		btnAchicar.addActionListener(this);
		btnAchicar.setBounds(567, 249, 89, 23);
		contentPane.add(btnAchicar);

	}

	@Override
	public void mouseClicked(MouseEvent e) {
		
		
	}

	@Override
	public void mousePressed(MouseEvent e) {
		
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		
		if(e.getSource() == btnEsquina) {
			btnEsquina.setSize(99,33);
		}else if(e.getSource() == btnCentro) {
			btnCentro.setSize(99,33);
		}else if(e.getSource() == btnAgrandar) {
			btnAgrandar.setSize(99,33);
		}else if(e.getSource() == btnAchicar) {
			btnAchicar.setSize(99,33);
		}
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		
		if(e.getSource() == btnEsquina) {
			btnEsquina.setSize(89,23);
		}else if(e.getSource() == btnCentro) {
			btnCentro.setSize(89,23);
		}else if(e.getSource() == btnAgrandar) {
			btnAgrandar.setSize(89,23);
		}else if(e.getSource() == btnAchicar) {
			btnAchicar.setSize(89,23);
		}
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		
		if(e.getSource() == btnEsquina) {
			lblNombre.setLocation(0,0);
		}else if(e.getSource() == btnCentro) {
			lblNombre.setLocation(290,180);
		}else if(e.getSource() == btnAgrandar) {
			lblNombre.setSize(180, 45);
		}else if(e.getSource() == btnAchicar) {
			lblNombre.setSize(160, 15);
		}
		
	}
	
	

}
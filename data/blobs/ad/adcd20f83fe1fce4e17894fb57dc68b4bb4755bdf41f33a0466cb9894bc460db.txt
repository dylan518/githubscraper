package gui;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import net.miginfocom.swing.MigLayout;
import javax.swing.JLabel;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;
import java.awt.Font;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;

public class Ejercicios2_8 extends JFrame {

	private JPanel contentPane;
	private JComboBox<String> cbxSel;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Ejercicios2_8 frame = new Ejercicios2_8();
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
	public Ejercicios2_8() {
		setTitle("Seleccione ciudad");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 422, 289);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(new MigLayout("", "[grow,fill][132.00][][170.00,grow][grow,fill]", "[grow,fill][][37.00][][grow,fill]"));
		
		JLabel lblNewLabel = new JLabel("Ciudad");
		lblNewLabel.setFont(new Font("Tahoma", Font.BOLD, 14));
		contentPane.add(lblNewLabel, "cell 1 1,alignx right,aligny baseline");
		
		cbxSel = new JComboBox<>();
		cbxSel.setFont(new Font("Tahoma", Font.ITALIC, 13));
		cbxSel.setModel(new DefaultComboBoxModel<String>(new String[] {"Adamuz", "Cabra", "Córdoba", "Lucena", "Montalbán", "Montilla", "Monturque"}));
		contentPane.add(cbxSel, "cell 3 1,growx");
		
		JLabel lblNewLabel_1 = new JLabel("Has seleccionado");
		lblNewLabel_1.setFont(new Font("Tahoma", Font.PLAIN, 14));
		contentPane.add(lblNewLabel_1, "cell 1 3");
		
		JLabel lblSel = new JLabel("");
		lblSel.setFont(new Font("Times New Roman", Font.BOLD, 14));
		contentPane.add(lblSel, "cell 3 3");
		
		cbxSel.addItemListener(new ItemListener()
		{
			public void itemStateChanged(ItemEvent e)
			{
				lblSel.setText(cbxSel.getSelectedItem().toString());
			}
		});
	}

}

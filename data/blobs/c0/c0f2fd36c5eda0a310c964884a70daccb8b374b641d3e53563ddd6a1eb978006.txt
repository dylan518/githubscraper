/**
 * @(#)fgawai.java
 *
 *
 * @author 
 * @version 1.00 2020/3/24
 */

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;
import java.sql.*;

public class fgawai extends JFrame implements ActionListener {
	
	private JPanel 	pPgw       = new JPanel();
	private JLabel 	lNip	   = new JLabel ("N I P       "),
				lNama	   = new JLabel ("Nama        "), 
				lBagian    = new JLabel ("Bagian      "),
				lcreate    = new JLabel ("nama"); 
	private JTextField 	fNip	   = new JTextField (), 
				fNama	   = new JTextField (), 
				fBagian    = new JTextField ();
	private JButton 	btnAdd     = new JButton (),
	 			btnCari     = new JButton (),
				btnSelesai  = new JButton ();
	

    public fgawai() {
    	setPreferredSize(new Dimension(450,280));
		setTitle("Data Pegawai");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JDesktopPane pPgw = new JDesktopPane();
		
		/* Mengatur letak objek Label Di container*/
		lNip.setBounds (15, 20, 100, 25);
	       lNama.setBounds (15, 55, 100, 25);
		lBagian.setBounds (15, 90, 100, 25);
		lcreate.setBounds (250, 210, 200, 25);
		lcreate.setText("create by nama dan nim Anda");
        
		/* Mengatur letak objek Text Di Container */
		fNip.setBounds (115, 20, 100, 25);
		fNama.setBounds (115, 55, 205, 25);
		fBagian.setBounds (115, 90, 92, 25);
		fNip.setToolTipText("Isi Nip dengan Angka !");

		/* Mengatur letak objek Button di Container */
		btnAdd.setBounds (150, 150, 85, 25);	
		btnAdd.setLabel("Add");	
		btnAdd.setBackground(Color.red);
		btnAdd.setForeground(Color.getHSBColor(250,0,255));
		btnCari.setBounds (50, 150, 85, 25);
		btnCari.setLabel("Cari");
		btnSelesai.setBounds (250, 150, 85, 25);
		btnSelesai.setLabel("Selesai");
		btnSelesai.setToolTipText("Mengakhiri Program");
     
		/* Objek Button di Non Aktifkan dan di aktifkan */
		btnAdd.setEnabled(true);		
		btnSelesai.setEnabled(true);			

		// Mengatur objek untuk dapat berinteraksi
		btnAdd.addActionListener (this);
		btnCari.addActionListener (this);
		btnSelesai.addActionListener (this);

		
		// Meletakkan seluruh kontrol pada objek panel */
		pPgw.add (lNip);	
		pPgw.add (fNip);
		pPgw.add (lNama);	
		pPgw.add (fNama);
		pPgw.add (lBagian);		
		pPgw.add (fBagian);
		pPgw.add (lcreate); 
		pPgw.add (btnCari);	
		pPgw.add (btnAdd);		
		pPgw.add (btnSelesai);
		
		/* Menambahkan objek panel (pPgr) ke container frame */
		getContentPane().add (pPgw).setBackground(Color.getHSBColor(250,0,255));
		
		/* Menampilkan frame ke layar monitor */
		pack();

    }
    
    public static void main(String[] args) {
		new fgawai().setVisible(true);
	}
	
	/* Fungsi jika user melakukan action penekanan tombol Button */
	public void actionPerformed (ActionEvent ae) {
		Object obj = ae.getSource();

		if (obj == btnAdd) 	
		{ 
			//Add();
		}				
		if (obj == btnSelesai) 	
		{ 
			System.exit(0);	
		}			
	}
	
	// Fungsi untuk menambahkan data ke tabel
	void Add()
	{
		//kode perintah insert tabel
	}
	
	// Fungsi untuk mengkosongkan Objek masukan 
	void Kosong () 
	{
		 fNip.setText ("");
		 fNama.setText ("");
		 fBagian.setText ("");
		 btnAdd.setEnabled(true);
 		 btnSelesai.setEnabled(true);
		 fNip.requestFocus ();
      }    
}
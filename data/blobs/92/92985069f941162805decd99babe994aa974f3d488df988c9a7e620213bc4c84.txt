package org.test.tugas.imam;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Registrasi implements ActionListener {
    String judul;
    JTextField txtNim;
    JTextField txtNama;
    JTextField txtAlamat;
    JButton btnCari;
    JButton btnSimpan;

    public Registrasi(String jd) {
        JFrame tampil = new JFrame();
        tampil.setLayout(null);
        tampil.setVisible(true);

        JLabel lblJudul = new JLabel(jd);
        lblJudul.setBounds(50, 10, 200, 30);
        tampil.add(lblJudul);

        JLabel lblNim = new JLabel("Nim");
        lblNim.setBounds(20, 40, 100, 30);
        tampil.add(lblNim);

        txtNim = new JTextField(50);
        txtNim.setBounds(70, 40, 120, 30);
        tampil.add(txtNim);

        btnCari = new JButton("Cari");
        btnCari.setBounds(200, 40, 100, 30);
        btnCari.addActionListener(this);
        tampil.add(btnCari);

        JLabel lblNama = new JLabel("Nama");
        lblNama.setBounds(20, 80, 100, 30);
        tampil.add(lblNama);

        txtNama = new JTextField(50);
        txtNama.setBounds(70, 80, 120, 30);
        tampil.add(txtNama);

        JLabel lblAlamat = new JLabel("Alamat");
        lblAlamat.setBounds(20, 120, 100, 30);
        tampil.add(lblAlamat);

        txtAlamat = new JTextField(50);
        txtAlamat.setBounds(70, 120, 120, 30);
        tampil.add(txtAlamat);

        btnSimpan = new JButton("Simpan Data");
        btnSimpan.setBounds(40, 150, 150, 30);
        btnSimpan.addActionListener(this);
        tampil.add(btnSimpan);

        tampil.setSize(400, 300);
        tampil.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    @Override
public void actionPerformed(ActionEvent arg0) {
    try {
        Connection koneksi = DriverManager.getConnection("jdbc:mysql://localhost/vis3_kamis", "root", "");
        Statement stm = koneksi.createStatement();

        if (arg0.getSource() == btnSimpan) {
            stm.executeUpdate("insert into tm_mahasiswa values ('" + txtNim.getText() + "', '" + txtNama.getText() + "', '" + txtAlamat.getText() + "')");
            JOptionPane.showMessageDialog(null, "Insert Data");
            txtNim.setText("");
            txtNama.setText("");
            txtAlamat.setText("");
        } else if (arg0.getSource() == btnCari) {
            ResultSet hasil = stm.executeQuery("SELECT * FROM tm_mahasiswa where NIM='" + txtNim.getText() + "'");
            while (hasil.next()) {
                txtNama.setText(hasil.getString(2));
                txtAlamat.setText(hasil.getString(3));
            }
        }

    } catch (Exception e) {
        e.printStackTrace();
    }
}

}
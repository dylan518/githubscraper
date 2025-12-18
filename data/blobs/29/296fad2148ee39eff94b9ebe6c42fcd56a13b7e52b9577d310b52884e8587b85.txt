
import java.awt.Color;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableModel;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author yassine
 */
public class Serveur extends javax.swing.JFrame {

    /**
     * Creates new form Serveur
     */
      Statement stat=null;
    MysqlConnect  maConnexion=new MysqlConnect();
    Connection conn=null;
    PreparedStatement pst=null;
    ResultSet rs=null;
    
    public Serveur() {
        initComponents();
        getContentPane().setBackground(Color.white);
       
       /* Affectation a=new Affectation();
        
        a.setVisible(true);
        this.setVisible(false);*/
        
        txt_DP.setText("DP-KH-01");
        txt_css.setText("PHONE-DID-KH");
        txt_F1.setText("CSS-ON-NET-FWD");
        txt_LCss.setText("LNCSS-LOBY");
        txt_Rp.setText("PT-ON-NET");
        
        setTitle("To Serveur");
         DefaultTableModel model= new DefaultTableModel();
   
   model.addColumn("MAC Address/Device Name (String[12/50] MANDATORY)");
   model.addColumn("Description (String [128] OPTIONAL )");
   model.addColumn("Device Pool (String[50] OPTIONAL)");
   model.addColumn("CSS (String[50] OPTIONAL)");
   model.addColumn("ASCII Alerting Name  1 (String [30] OPTIONAL )");
   model.addColumn("ASCII Display  1 (String [30] OPTIONAL )");
   model.addColumn("Alerting Name  1 (String [50] OPTIONAL )");
   model.addColumn("ASCII Line Text Label  1 (String [30] OPTIONAL )");
   model.addColumn("Directory Number  1 (Integer [255] OPTIONAL )");
   model.addColumn("Display  1 (String [120] OPTIONAL )");
   model.addColumn("Forward All CSS  1 (String [50] OPTIONAL )");
   model.addColumn("Line CSS  1 (String [50] OPTIONAL )");
   model.addColumn("Line Text Label 1(String [120] OPTIONAL )");
   model.addColumn("Route Partition  1 (String [50] OPTIONAL )");
   
   
   TableServeur.setModel(model);
   String requette="select * from serveur";
   try{
       
        stat=MysqlConnect.ConnectDB().createStatement();
        ResultSet rs=stat.executeQuery(requette);
        while(rs.next()){
     //   model.addRow(new Object[]{rs.getInt("id"),rs.getString("MAC Address/Device Name (String[12/50] MANDATORY)"),rs.getString("Description (String [128] OPTIONAL )"),rs.getString("Description (String [128] OPTIONAL )"),rs.getString("CSS (String[50] OPTIONAL)"),rs.getString("ASCII Alerting Name 1 (String [30] OPTIONAL )"),rs.getString("ASCII Display  1 (String [30] OPTIONAL )"),rs.getString("Alerting Name  1 (String [50] OPTIONAL )"),rs.getString("ASCII Line Text Label  1 (String [30] OPTIONAL )"),rs.getString("Directory Number 1 (Integer [255] OPTIONAL )"),rs.getString("Display 1 (String [120] OPTIONAL )"),rs.getString("Forward All CSS 1 (String [50] OPTIONAL )"),rs.getString("Line CSS  1 (String [50] OPTIONAL )"),rs.getString("Line Text Label 1(String [120] OPTIONAL )"),rs.getString("Route Partition  1 (String [50] OPTIONAL )")} );
        
        model.addRow(new Object[]{rs.getString("MAC Address/Device Name (String[12/50] MANDATORY)"),rs.getString("Description (String [128] OPTIONAL )"),rs.getString("Device Pool (String[50] OPTIONAL)"),rs.getString("CSS (String[50] OPTIONAL)"),rs.getString("ASCII Alerting Name 1 (String [30] OPTIONAL )"),rs.getString("ASCII Display  1 (String [30] OPTIONAL )"),rs.getString("Alerting Name  1 (String [50] OPTIONAL )"),rs.getString("ASCII Line Text Label 1 (String [30] OPTIONAL )"),rs.getString("Directory Number 1 (Integer [255] OPTIONAL )"),rs.getString("Display 1 (String [120] OPTIONAL )"),rs.getString("Forward All CSS  1 (String [50] OPTIONAL )"),rs.getString("Line CSS 1 (String [50] OPTIONAL )"),rs.getString("Line Text Label 1(String [120] OPTIONAL )"),rs.getString("Route Partition 1 (String [50] OPTIONAL )")} );
        }
         
   }catch(SQLException ex){
       JOptionPane.showMessageDialog(null, ex);
    };
    }
    public void toExcel(JTable table, File file){
		try{
			TableModel model = table.getModel();
			FileWriter excel = new FileWriter(file);

			for(int i = 0; i < model.getColumnCount(); i++){
				excel.write(model.getColumnName(i) + "\t");
			}

			excel.write("\n");

			for(int i=0; i< model.getRowCount(); i++) {
				for(int j=0; j < model.getColumnCount(); j++) {
					excel.write(model.getValueAt(i,j).toString()+"\t");
				}
				excel.write("\n");
			}

			excel.close();
		}catch(IOException e){ System.out.println(e); }
	}

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jScrollPane1 = new javax.swing.JScrollPane();
        TableServeur = new javax.swing.JTable();
        jButton1 = new javax.swing.JButton();
        btn_inserer = new javax.swing.JButton();
        jButton3 = new javax.swing.JButton();
        btn_Taffe1 = new javax.swing.JButton();
        jPanel1 = new javax.swing.JPanel();
        txt_D1 = new javax.swing.JTextField();
        txt_F1 = new javax.swing.JTextField();
        txt_AssL = new javax.swing.JTextField();
        jLabel6 = new javax.swing.JLabel();
        laDP = new javax.swing.JLabel();
        laAscci = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        txt_Ass = new javax.swing.JTextField();
        txt_AN = new javax.swing.JTextField();
        jLabel5 = new javax.swing.JLabel();
        txt_DP = new javax.swing.JTextField();
        txt_AssD = new javax.swing.JTextField();
        txt_css = new javax.swing.JTextField();
        laD = new javax.swing.JLabel();
        txt_LCss = new javax.swing.JTextField();
        jLabel1 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        txt_Rp = new javax.swing.JTextField();
        jLabel8 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        txt_AM = new javax.swing.JTextField();
        txt_Desp = new javax.swing.JTextField();
        jLabel9 = new javax.swing.JLabel();
        laAm = new javax.swing.JLabel();
        txt_DN = new javax.swing.JTextField();
        txt_LT1 = new javax.swing.JTextField();
        jLabel7 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        btn_inserer1 = new javax.swing.JButton();
        btn_inserer2 = new javax.swing.JButton();
        jButton4 = new javax.swing.JButton();
        jLabel11 = new javax.swing.JLabel();
        jMenuBar1 = new javax.swing.JMenuBar();
        jMenu1 = new javax.swing.JMenu();
        jMenu2 = new javax.swing.JMenu();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        TableServeur.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "Title 1", "Title 2", "Title 3", "Title 4"
            }
        ));
        TableServeur.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                TableServeurMouseClicked(evt);
            }
        });
        jScrollPane1.setViewportView(TableServeur);

        jButton1.setBackground(new java.awt.Color(67, 174, 76));
        jButton1.setIcon(new javax.swing.ImageIcon("C:\\Program Files\\NetBeans 8.0.2\\icons\\Excel.png")); // NOI18N
        jButton1.setText("Exporter Excel");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        btn_inserer.setBackground(new java.awt.Color(67, 174, 76));
        btn_inserer.setIcon(new javax.swing.ImageIcon("C:\\Program Files\\NetBeans 8.0.2\\icons\\quitter.png")); // NOI18N
        btn_inserer.setText("Quitter");
        btn_inserer.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_insererActionPerformed(evt);
            }
        });

        jButton3.setBackground(new java.awt.Color(67, 174, 76));
        jButton3.setIcon(new javax.swing.ImageIcon("C:\\Program Files\\NetBeans 8.0.2\\icons\\PDF.png")); // NOI18N
        jButton3.setText("Exporter PDF");
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });

        btn_Taffe1.setBackground(new java.awt.Color(67, 174, 76));
        btn_Taffe1.setIcon(new javax.swing.ImageIcon("C:\\Program Files\\NetBeans 8.0.2\\icons\\Home-.png")); // NOI18N
        btn_Taffe1.setText("Accueil");

        jPanel1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(67, 174, 76), 2));

        txt_F1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txt_F1ActionPerformed(evt);
            }
        });

        jLabel6.setText("Display  1 ");

        laDP.setText("Device Pool ");

        laAscci.setText("ASCII Display  1 ");

        jLabel10.setText("Route Partition  1 ");

        jLabel5.setText("CSS ");

        laD.setText("Description ");

        jLabel1.setText("Alerting Name  1 ");

        jLabel4.setText("Directory Number  1 ");

        jLabel8.setText("Line CSS  1");

        jLabel2.setText("ASCII Line Text Label  1 ");

        txt_AM.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txt_AMActionPerformed(evt);
            }
        });

        jLabel9.setText("Line Text Label  1");

        laAm.setText("MAC Address/Device Name");

        jLabel7.setText("Forward All CSS  1");

        jLabel3.setText("ASCII Alerting Name  1 ");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel5)
                    .addComponent(laAscci)
                    .addComponent(jLabel3)
                    .addComponent(jLabel2)
                    .addComponent(jLabel4)
                    .addComponent(jLabel6)
                    .addComponent(jLabel7)
                    .addComponent(jLabel8)
                    .addComponent(jLabel1)
                    .addComponent(jLabel9)
                    .addComponent(jLabel10)
                    .addComponent(laD)
                    .addComponent(laAm)
                    .addComponent(laDP))
                .addGap(57, 57, 57)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                    .addComponent(txt_css)
                    .addComponent(txt_Desp)
                    .addComponent(txt_AM)
                    .addComponent(txt_DP)
                    .addComponent(txt_AssD)
                    .addComponent(txt_Rp)
                    .addComponent(txt_LT1)
                    .addComponent(txt_D1)
                    .addComponent(txt_DN)
                    .addComponent(txt_AssL)
                    .addComponent(txt_AN)
                    .addComponent(txt_F1)
                    .addComponent(txt_LCss)
                    .addComponent(txt_Ass, javax.swing.GroupLayout.PREFERRED_SIZE, 96, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(26, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(17, 17, 17)
                        .addComponent(laAm)
                        .addGap(16, 16, 16)
                        .addComponent(laD)
                        .addGap(12, 12, 12)
                        .addComponent(laDP)
                        .addGap(24, 24, 24)
                        .addComponent(jLabel5)
                        .addGap(12, 12, 12)
                        .addComponent(jLabel3)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(laAscci)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel1)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel2)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel4)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel6)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel7)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel8)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel9)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel10))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(txt_AM, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(txt_Desp, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(txt_DP, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_css, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_Ass, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_AssD, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_AN, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(txt_AssL, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_DN, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_D1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_F1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_LCss, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_LT1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(txt_Rp, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap())
        );

        btn_inserer1.setBackground(new java.awt.Color(67, 174, 76));
        btn_inserer1.setIcon(new javax.swing.ImageIcon("C:\\Program Files\\NetBeans 8.0.2\\icons\\editer.png")); // NOI18N
        btn_inserer1.setText("Modifier");
        btn_inserer1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_inserer1ActionPerformed(evt);
            }
        });

        btn_inserer2.setBackground(new java.awt.Color(67, 174, 76));
        btn_inserer2.setIcon(new javax.swing.ImageIcon("C:\\Program Files\\NetBeans 8.0.2\\icons\\poubelle.png")); // NOI18N
        btn_inserer2.setText("Supprimer");
        btn_inserer2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_inserer2ActionPerformed(evt);
            }
        });

        jButton4.setBackground(new java.awt.Color(67, 174, 76));
        jButton4.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Excel2.png"))); // NOI18N
        jButton4.setText("Exporter .CSV");
        jButton4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton4ActionPerformed(evt);
            }
        });

        jLabel11.setBackground(new java.awt.Color(255, 255, 255));
        jLabel11.setFont(new java.awt.Font("Tahoma", 1, 24)); // NOI18N
        jLabel11.setForeground(new java.awt.Color(67, 174, 76));
        jLabel11.setText("Serveur");

        jMenu1.setText("File");
        jMenuBar1.add(jMenu1);

        jMenu2.setText("Edit");
        jMenuBar1.add(jMenu2);

        setJMenuBar(jMenuBar1);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(btn_Taffe1, javax.swing.GroupLayout.PREFERRED_SIZE, 99, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jButton1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jButton4)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jButton3, javax.swing.GroupLayout.PREFERRED_SIZE, 126, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(29, 29, 29)
                .addComponent(btn_inserer1, javax.swing.GroupLayout.PREFERRED_SIZE, 109, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(31, 31, 31)
                .addComponent(btn_inserer2, javax.swing.GroupLayout.PREFERRED_SIZE, 116, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(26, 26, 26)
                .addComponent(btn_inserer, javax.swing.GroupLayout.PREFERRED_SIZE, 111, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(layout.createSequentialGroup()
                .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 714, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(381, 381, 381)
                        .addComponent(jLabel11, javax.swing.GroupLayout.PREFERRED_SIZE, 99, javax.swing.GroupLayout.PREFERRED_SIZE))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addGap(25, 25, 25))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(21, 21, 21)
                        .addComponent(jLabel11)
                        .addGap(18, 18, 18)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btn_Taffe1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jButton1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jButton4, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jButton3)
                    .addComponent(btn_inserer1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(btn_inserer2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(btn_inserer, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addGap(69, 69, 69))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void txt_AMActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txt_AMActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txt_AMActionPerformed

    private void TableServeurMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_TableServeurMouseClicked
        txt_DP.setText("DP-KH-01");
        txt_css.setText("PHONE-DID-KH");
        txt_F1.setText("CSS-ON-NET-FWD");
        txt_LCss.setText("LNCSS-LOBY");
        txt_Rp.setText("PT-ON-NET");
    }//GEN-LAST:event_TableServeurMouseClicked

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        JFileChooser fc = new JFileChooser();
                int option = fc.showSaveDialog(Serveur.this);
                if(option == JFileChooser.APPROVE_OPTION){
                    String filename = fc.getSelectedFile().getName(); 
                    String path = fc.getSelectedFile().getParentFile().getPath();

					int len = filename.length();
					String ext = "";
					String file = "";

					if(len > 4){
						ext = filename.substring(len-4, len);
					}

					if(ext.equals(".xls")){
						file = path + "\\" + filename; 
					}else{
						file = path + "\\" + filename + ".xls"; 
					}
					toExcel(TableServeur, new File(file));
                                        JOptionPane.showMessageDialog(null, "Enregistré avec succés à"+path+" ");
				}
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
        
    }//GEN-LAST:event_jButton3ActionPerformed

    private void btn_insererActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_insererActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btn_insererActionPerformed

    private void btn_inserer1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_inserer1ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btn_inserer1ActionPerformed

    private void btn_inserer2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_inserer2ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btn_inserer2ActionPerformed

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton4ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_jButton4ActionPerformed

    private void txt_F1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txt_F1ActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txt_F1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Serveur.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Serveur.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Serveur.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Serveur.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Serveur().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JTable TableServeur;
    private javax.swing.JButton btn_Taffe1;
    private javax.swing.JButton btn_inserer;
    private javax.swing.JButton btn_inserer1;
    private javax.swing.JButton btn_inserer2;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JMenu jMenu1;
    private javax.swing.JMenu jMenu2;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JLabel laAm;
    private javax.swing.JLabel laAscci;
    private javax.swing.JLabel laD;
    private javax.swing.JLabel laDP;
    public static javax.swing.JTextField txt_AM;
    public static javax.swing.JTextField txt_AN;
    public static javax.swing.JTextField txt_Ass;
    public static javax.swing.JTextField txt_AssD;
    public static javax.swing.JTextField txt_AssL;
    public static javax.swing.JTextField txt_D1;
    public static javax.swing.JTextField txt_DN;
    public static javax.swing.JTextField txt_DP;
    public static javax.swing.JTextField txt_Desp;
    public static javax.swing.JTextField txt_F1;
    public static javax.swing.JTextField txt_LCss;
    public static javax.swing.JTextField txt_LT1;
    public static javax.swing.JTextField txt_Rp;
    public static javax.swing.JTextField txt_css;
    // End of variables declaration//GEN-END:variables
}

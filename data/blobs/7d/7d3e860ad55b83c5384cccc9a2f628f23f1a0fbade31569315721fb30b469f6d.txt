
package Presentacion;

import java.awt.Image;
import java.awt.Toolkit;
import javax.swing.JOptionPane;


public class frm_login extends javax.swing.JFrame {

    public frm_login() {
        initComponents();
        this.setLocationRelativeTo(null); // ejecuta el codigo en el centro de la pantalla
        getIconImage();
    }

    public Image getIconImage() {
        Image retValue = Toolkit.getDefaultToolkit().getImage(ClassLoader.getSystemResource("Imagenes/logo.png"));
        return retValue;
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        txt_user = new javax.swing.JTextField();
        jpf_contraseña = new javax.swing.JPasswordField();
        btn_sesion = new javax.swing.JButton();
        btn_salir1 = new javax.swing.JButton();
        jLabelfondo = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setUndecorated(true);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setFont(new java.awt.Font("Times New Roman", 3, 24)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(255, 255, 255));
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Imagenes/contrasena.png"))); // NOI18N
        jLabel1.setText("Contraseña :");
        getContentPane().add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(30, 450, -1, -1));

        jLabel2.setFont(new java.awt.Font("Times New Roman", 3, 24)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(255, 255, 255));
        jLabel2.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel2.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Imagenes/usuario.png"))); // NOI18N
        jLabel2.setText("Usuario :");
        getContentPane().add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 390, 140, -1));

        jLabel3.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Imagenes/logo.png"))); // NOI18N
        getContentPane().add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(100, 30, -1, -1));

        txt_user.setBackground(new java.awt.Color(0, 0, 102));
        txt_user.setFont(new java.awt.Font("Times New Roman", 1, 14)); // NOI18N
        txt_user.setForeground(new java.awt.Color(255, 255, 255));
        txt_user.setHorizontalAlignment(javax.swing.JTextField.CENTER);
        txt_user.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txt_userActionPerformed(evt);
            }
        });
        getContentPane().add(txt_user, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 390, 170, 30));

        jpf_contraseña.setBackground(new java.awt.Color(0, 0, 102));
        jpf_contraseña.setFont(new java.awt.Font("Times New Roman", 1, 14)); // NOI18N
        jpf_contraseña.setForeground(new java.awt.Color(255, 255, 255));
        jpf_contraseña.setHorizontalAlignment(javax.swing.JTextField.CENTER);
        getContentPane().add(jpf_contraseña, new org.netbeans.lib.awtextra.AbsoluteConstraints(200, 450, 170, 30));

        btn_sesion.setBackground(new java.awt.Color(0, 0, 102));
        btn_sesion.setFont(new java.awt.Font("Times New Roman", 1, 14)); // NOI18N
        btn_sesion.setForeground(new java.awt.Color(255, 255, 255));
        btn_sesion.setText("Iniciar Sesión");
        btn_sesion.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_sesionActionPerformed(evt);
            }
        });
        getContentPane().add(btn_sesion, new org.netbeans.lib.awtextra.AbsoluteConstraints(370, 510, -1, -1));

        btn_salir1.setBackground(new java.awt.Color(153, 0, 0));
        btn_salir1.setFont(new java.awt.Font("Times New Roman", 1, 14)); // NOI18N
        btn_salir1.setForeground(new java.awt.Color(255, 255, 255));
        btn_salir1.setText("Salir");
        btn_salir1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btn_salir1ActionPerformed(evt);
            }
        });
        getContentPane().add(btn_salir1, new org.netbeans.lib.awtextra.AbsoluteConstraints(430, 0, -1, -1));

        jLabelfondo.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Imagenes/fondo.png"))); // NOI18N
        getContentPane().add(jLabelfondo, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 494, -1));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void txt_userActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txt_userActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txt_userActionPerformed

    private void btn_salir1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_salir1ActionPerformed
        System.exit(0);
    }//GEN-LAST:event_btn_salir1ActionPerformed

    private void btn_sesionActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btn_sesionActionPerformed
        String user = "";
        String password = "";
        user = txt_user.getText();
        password = jpf_contraseña.getText();
        frm_principal home = new frm_principal();
        if (password.equals("user") & user.equals("user")) {
            home.setVisible(true);
            this.dispose();
        } else {
            JOptionPane.showMessageDialog(this, "Datos incorrectos. Por favor volver a intentar");
        }
    }//GEN-LAST:event_btn_sesionActionPerformed

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
            java.util.logging.Logger.getLogger(frm_login.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(frm_login.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(frm_login.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(frm_login.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new frm_login().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btn_salir1;
    private javax.swing.JButton btn_sesion;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabelfondo;
    private javax.swing.JPasswordField jpf_contraseña;
    private javax.swing.JTextField txt_user;
    // End of variables declaration//GEN-END:variables
}

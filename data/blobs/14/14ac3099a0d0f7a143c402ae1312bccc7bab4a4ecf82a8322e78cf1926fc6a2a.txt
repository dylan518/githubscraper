/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package Presentacion;
import Conexion.UsuarioRepertorio;

import Negocio.Libro;
import Negocio.Usuario;
import Presentacion.Contenido.*;
import com.formdev.flatlaf.FlatIntelliJLaf;
import com.formdev.flatlaf.FlatLightLaf;
import com.formdev.flatlaf.intellijthemes.materialthemeuilite.FlatMaterialDarkerIJTheme;
import com.formdev.flatlaf.intellijthemes.materialthemeuilite.FlatMaterialLighterIJTheme;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import javax.swing.UIManager;
import java.awt.BorderLayout;
import java.util.List;
import javax.swing.JPanel;
import javax.swing.border.Border;
import javax.swing.JFrame;

public class Menu extends javax.swing.JFrame {
    /**
     * Creates new form Menu
     */
    public Menu() {
        initComponents();
        SetDate();
        estilo();
        Inicio();
        MiVentana();
        System.out.println(UsuarioRepertorio.existeUsuario(7));
        System.out.println(UsuarioRepertorio.existeLibro("100"));
    }
    private void Inicio(){
        mostrar(new Principal());
    }
    
    public void MiVentana() {
        setTitle("Universidad Tecnológica del Perú");
        setSize(1020,638);  // Tamaño inicial de la ventana
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setResizable(false);
    }
    public static void mostrar (JPanel j){
        j.setSize(750,390);
        j.setLocation(0,0);
        Contenido.removeAll();
        Contenido.add(j,BorderLayout.CENTER);
        Contenido.revalidate();
        Contenido.repaint();
    }
    private void estilo() {
        titulo.putClientProperty( "FlatLaf.styleClass", "h00" );
    }
        private void SetDate() {
        LocalDate now = LocalDate.now();
        Locale spanishLocale = new Locale("es", "ES");
        datetxt.setText(now.format(DateTimeFormatter.ofPattern("'Hoy es' EEEE dd 'de' MMMM 'de' yyyy", spanishLocale)));
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jProgressBar1 = new javax.swing.JProgressBar();
        jMenuBar2 = new javax.swing.JMenuBar();
        jMenu3 = new javax.swing.JMenu();
        jMenu4 = new javax.swing.JMenu();
        Fondo = new javax.swing.JPanel();
        Menu = new javax.swing.JPanel();
        jSeparator1 = new javax.swing.JSeparator();
        jLabel2 = new javax.swing.JLabel();
        jPanel1 = new javax.swing.JPanel();
        reportes = new javax.swing.JButton();
        Principal = new javax.swing.JButton();
        prestamos = new javax.swing.JButton();
        Libros = new javax.swing.JButton();
        devolver = new javax.swing.JButton();
        usuarios = new javax.swing.JButton();
        jPanel2 = new javax.swing.JPanel();
        datetxt = new javax.swing.JLabel();
        titulo = new javax.swing.JLabel();
        jLabel1 = new javax.swing.JLabel();
        Contenido = new javax.swing.JPanel();

        jMenu3.setText("File");
        jMenuBar2.add(jMenu3);

        jMenu4.setText("Edit");
        jMenuBar2.add(jMenu4);

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setMaximizedBounds(new java.awt.Rectangle(250, 190, 0, 0));
        setMinimumSize(new java.awt.Dimension(1020, 600));

        Fondo.setBackground(new java.awt.Color(255, 255, 255));
        Fondo.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));

        Menu.setBackground(new java.awt.Color(255, 0, 51));
        Menu.setForeground(new java.awt.Color(255, 0, 0));
        Menu.setPreferredSize(new java.awt.Dimension(270, 620));

        jSeparator1.setForeground(new java.awt.Color(255, 255, 255));

        jLabel2.setIcon(new javax.swing.ImageIcon(getClass().getResource("/asociados_UTP.png"))); // NOI18N

        jPanel1.setBackground(new java.awt.Color(255, 255, 255));
        jPanel1.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        reportes.setBackground(new java.awt.Color(204, 0, 0));
        reportes.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        reportes.setForeground(new java.awt.Color(255, 255, 255));
        reportes.setIcon(new javax.swing.ImageIcon(getClass().getResource("/file-chart.png"))); // NOI18N
        reportes.setText("Reportes");
        reportes.setBorder(javax.swing.BorderFactory.createMatteBorder(1, 15, 1, 1, new java.awt.Color(0, 0, 0)));
        reportes.setBorderPainted(false);
        reportes.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        reportes.setIconTextGap(10);
        reportes.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                reportesActionPerformed(evt);
            }
        });
        jPanel1.add(reportes, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 250, 270, 50));

        Principal.setBackground(new java.awt.Color(204, 0, 0));
        Principal.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        Principal.setForeground(new java.awt.Color(255, 255, 255));
        Principal.setIcon(new javax.swing.ImageIcon(getClass().getResource("/home-outline.png"))); // NOI18N
        Principal.setText("Principal");
        Principal.setBorder(javax.swing.BorderFactory.createMatteBorder(1, 15, 1, 1, new java.awt.Color(0, 0, 0)));
        Principal.setBorderPainted(false);
        Principal.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        Principal.setIconTextGap(10);
        Principal.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                PrincipalActionPerformed(evt);
            }
        });
        jPanel1.add(Principal, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 270, 50));

        prestamos.setBackground(new java.awt.Color(204, 0, 0));
        prestamos.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        prestamos.setForeground(new java.awt.Color(255, 255, 255));
        prestamos.setIcon(new javax.swing.ImageIcon(getClass().getResource("/calendar-plus.png"))); // NOI18N
        prestamos.setText("Prestamos");
        prestamos.setBorder(javax.swing.BorderFactory.createMatteBorder(1, 15, 1, 1, new java.awt.Color(0, 0, 0)));
        prestamos.setBorderPainted(false);
        prestamos.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        prestamos.setIconTextGap(10);
        prestamos.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                prestamosActionPerformed(evt);
            }
        });
        jPanel1.add(prestamos, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 100, 270, 50));

        Libros.setBackground(new java.awt.Color(204, 0, 0));
        Libros.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        Libros.setForeground(new java.awt.Color(255, 255, 255));
        Libros.setIcon(new javax.swing.ImageIcon(getClass().getResource("/book-open-page-variant.png"))); // NOI18N
        Libros.setText("Libros ");
        Libros.setToolTipText("");
        Libros.setBorder(javax.swing.BorderFactory.createMatteBorder(1, 15, 1, 1, new java.awt.Color(0, 0, 0)));
        Libros.setBorderPainted(false);
        Libros.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        Libros.setIconTextGap(10);
        Libros.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                LibrosActionPerformed(evt);
            }
        });
        jPanel1.add(Libros, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 50, 270, 50));

        devolver.setBackground(new java.awt.Color(204, 0, 0));
        devolver.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        devolver.setForeground(new java.awt.Color(255, 255, 255));
        devolver.setIcon(new javax.swing.ImageIcon(getClass().getResource("/calendar-multiple-check.png"))); // NOI18N
        devolver.setText("Devoluciones");
        devolver.setBorder(javax.swing.BorderFactory.createMatteBorder(1, 15, 1, 1, new java.awt.Color(0, 0, 0)));
        devolver.setBorderPainted(false);
        devolver.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        devolver.setIconTextGap(10);
        devolver.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                devolverActionPerformed(evt);
            }
        });
        jPanel1.add(devolver, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 150, 270, 50));

        usuarios.setBackground(new java.awt.Color(204, 0, 0));
        usuarios.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        usuarios.setForeground(new java.awt.Color(255, 255, 255));
        usuarios.setIcon(new javax.swing.ImageIcon(getClass().getResource("/account-multiple.png"))); // NOI18N
        usuarios.setText("Usuarios");
        usuarios.setBorder(javax.swing.BorderFactory.createMatteBorder(1, 15, 1, 1, new java.awt.Color(0, 0, 0)));
        usuarios.setBorderPainted(false);
        usuarios.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        usuarios.setIconTextGap(10);
        usuarios.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                usuariosActionPerformed(evt);
            }
        });
        jPanel1.add(usuarios, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 200, 270, 50));

        javax.swing.GroupLayout MenuLayout = new javax.swing.GroupLayout(Menu);
        Menu.setLayout(MenuLayout);
        MenuLayout.setHorizontalGroup(
            MenuLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(MenuLayout.createSequentialGroup()
                .addGroup(MenuLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(MenuLayout.createSequentialGroup()
                        .addGap(25, 25, 25)
                        .addComponent(jLabel2))
                    .addGroup(MenuLayout.createSequentialGroup()
                        .addGap(30, 30, 30)
                        .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 200, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(250, 250, 250))
        );
        MenuLayout.setVerticalGroup(
            MenuLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(MenuLayout.createSequentialGroup()
                .addGap(18, 18, 18)
                .addComponent(jLabel2, javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(12, 12, 12)
                .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 20, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );

        jPanel2.setBackground(new java.awt.Color(0, 0, 0));
        jPanel2.setPreferredSize(new java.awt.Dimension(750, 150));

        datetxt.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        datetxt.setForeground(new java.awt.Color(255, 255, 255));
        datetxt.setText("Hoy es {dayname} {day} de {month} de {year}");

        titulo.setFont(new java.awt.Font("Trebuchet MS", 1, 36)); // NOI18N
        titulo.setForeground(new java.awt.Color(255, 255, 255));
        titulo.setText("GESTOR DE BIBLIOTECA");

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGap(66, 66, 66)
                        .addComponent(datetxt))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGap(58, 58, 58)
                        .addComponent(titulo)))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                .addContainerGap(43, Short.MAX_VALUE)
                .addComponent(titulo)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(datetxt)
                .addGap(27, 27, 27))
        );

        jLabel1.setFont(new java.awt.Font("Tahoma", 1, 12)); // NOI18N
        jLabel1.setText("Bienvenido <3");

        Contenido.setBackground(new java.awt.Color(255, 255, 255));
        Contenido.setPreferredSize(new java.awt.Dimension(750, 390));

        javax.swing.GroupLayout ContenidoLayout = new javax.swing.GroupLayout(Contenido);
        Contenido.setLayout(ContenidoLayout);
        ContenidoLayout.setHorizontalGroup(
            ContenidoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 750, Short.MAX_VALUE)
        );
        ContenidoLayout.setVerticalGroup(
            ContenidoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 410, Short.MAX_VALUE)
        );

        javax.swing.GroupLayout FondoLayout = new javax.swing.GroupLayout(Fondo);
        Fondo.setLayout(FondoLayout);
        FondoLayout.setHorizontalGroup(
            FondoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(FondoLayout.createSequentialGroup()
                .addComponent(Menu, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGroup(FondoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(FondoLayout.createSequentialGroup()
                        .addGap(5, 5, 5)
                        .addComponent(jLabel1))
                    .addComponent(jPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(Contenido, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
        );
        FondoLayout.setVerticalGroup(
            FondoLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(Menu, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
            .addGroup(FondoLayout.createSequentialGroup()
                .addGap(32, 32, 32)
                .addComponent(jLabel1)
                .addGap(13, 13, 13)
                .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, 0)
                .addComponent(Contenido, javax.swing.GroupLayout.PREFERRED_SIZE, 410, javax.swing.GroupLayout.PREFERRED_SIZE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(Fondo, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(Fondo, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void reportesActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_reportesActionPerformed
       mostrar(new Reportes());
    }//GEN-LAST:event_reportesActionPerformed

    private void PrincipalActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_PrincipalActionPerformed
       mostrar(new Principal());
    }//GEN-LAST:event_PrincipalActionPerformed

    private void prestamosActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_prestamosActionPerformed
        mostrar(new Prestar());
    }//GEN-LAST:event_prestamosActionPerformed

    private void devolverActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_devolverActionPerformed
       mostrar(new Devolver());
    }//GEN-LAST:event_devolverActionPerformed

    private void LibrosActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_LibrosActionPerformed
         mostrar(new Books());
    }//GEN-LAST:event_LibrosActionPerformed

    private void usuariosActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_usuariosActionPerformed
        mostrar(new Usuarios());
    }//GEN-LAST:event_usuariosActionPerformed

   
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
      
        FlatIntelliJLaf.setup();
        UIManager.put( "Button.arc", 999 );
        UIManager.put( "Component.arc", 999 );
        UIManager.put( "ProgressBar.arc", 999 );
        UIManager.put( "TextComponent.arc", 999 );
        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Menu().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private static javax.swing.JPanel Contenido;
    private javax.swing.JPanel Fondo;
    private javax.swing.JButton Libros;
    private javax.swing.JPanel Menu;
    private javax.swing.JButton Principal;
    private javax.swing.JLabel datetxt;
    private javax.swing.JButton devolver;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JMenu jMenu3;
    private javax.swing.JMenu jMenu4;
    private javax.swing.JMenuBar jMenuBar2;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JProgressBar jProgressBar1;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JButton prestamos;
    private javax.swing.JButton reportes;
    private javax.swing.JLabel titulo;
    private javax.swing.JButton usuarios;
    // End of variables declaration//GEN-END:variables
}

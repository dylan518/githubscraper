package Paneles;

import Clases.Proveedor;
import Consultas.ProveedorDao;
import java.awt.Window;
import javax.swing.JDialog;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;
import javax.swing.text.AbstractDocument;
import javax.swing.text.AttributeSet;
import javax.swing.text.BadLocationException;
import javax.swing.text.DocumentFilter;

public class PanelRegistroProveedor extends javax.swing.JPanel {

    ProveedorDao daoProveedor = new ProveedorDao();
    Proveedor prove = new Proveedor();

    public PanelRegistroProveedor() {
        initComponents();
        ValidarCampo();
        txtIdProveedor.setVisible(false);
    }

    private PanelProveedor panelProveedor;

    public void setPanelProveedor(PanelProveedor panelProveedor) {
        this.panelProveedor = panelProveedor;
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jPanel2 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        txtRucProveedor = new javax.swing.JTextField();
        txtNombreProveedor = new javax.swing.JTextField();
        chkActivoProveedor = new javax.swing.JCheckBox();
        jLabel4 = new javax.swing.JLabel();
        txtCelularProveedor = new javax.swing.JTextField();
        btnGuardarProveedor = new javax.swing.JButton();
        btnActualizarProveedor = new javax.swing.JButton();
        txtIdProveedor = new javax.swing.JLabel();

        jPanel1.setBackground(new java.awt.Color(255, 255, 255));

        jPanel2.setBackground(new java.awt.Color(255, 255, 255));
        jPanel2.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(41, 43, 45)), "DATOS DEL PROVEEDOR", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, new java.awt.Font("Book Antiqua", 0, 12))); // NOI18N

        jLabel1.setFont(new java.awt.Font("Book Antiqua", 0, 12)); // NOI18N
        jLabel1.setText("RUC PROVEEDOR:");

        jLabel2.setFont(new java.awt.Font("Book Antiqua", 0, 12)); // NOI18N
        jLabel2.setText("NOMBRE PROVEEDOR:");

        jLabel3.setFont(new java.awt.Font("Book Antiqua", 0, 12)); // NOI18N
        jLabel3.setText("ESTADO PROVEEDOR:");

        chkActivoProveedor.setFont(new java.awt.Font("Book Antiqua", 0, 12)); // NOI18N
        chkActivoProveedor.setText("Activo Proveedor");

        jLabel4.setFont(new java.awt.Font("Book Antiqua", 0, 12)); // NOI18N
        jLabel4.setText("CELULAR PROVEEDOR:");

        btnGuardarProveedor.setFont(new java.awt.Font("Book Antiqua", 0, 12)); // NOI18N
        btnGuardarProveedor.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imganes botones/guardar.png"))); // NOI18N
        btnGuardarProveedor.setText("GUARDAR PROVEEDOR");
        btnGuardarProveedor.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnGuardarProveedorActionPerformed(evt);
            }
        });

        btnActualizarProveedor.setFont(new java.awt.Font("Book Antiqua", 0, 12)); // NOI18N
        btnActualizarProveedor.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imganes botones/actualizar.png"))); // NOI18N
        btnActualizarProveedor.setText("ACTUALIZAR PROVEEDOR");
        btnActualizarProveedor.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnActualizarProveedorActionPerformed(evt);
            }
        });

        txtIdProveedor.setText("txtIdProveedor");

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jLabel2)
                            .addComponent(jLabel4)
                            .addComponent(jLabel1))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(txtCelularProveedor)
                            .addComponent(txtNombreProveedor)
                            .addComponent(txtRucProveedor)))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel2Layout.createSequentialGroup()
                                .addComponent(jLabel3)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(chkActivoProveedor)
                                .addGap(46, 46, 46)
                                .addComponent(txtIdProveedor))
                            .addGroup(jPanel2Layout.createSequentialGroup()
                                .addComponent(btnGuardarProveedor)
                                .addGap(18, 18, 18)
                                .addComponent(btnActualizarProveedor)))
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addGap(15, 15, 15)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(txtRucProveedor, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel1))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2)
                    .addComponent(txtNombreProveedor, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(txtCelularProveedor, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(9, 9, 9)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(jLabel3)
                    .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(chkActivoProveedor)
                        .addComponent(txtIdProveedor)))
                .addGap(18, 18, 18)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(btnGuardarProveedor)
                    .addComponent(btnActualizarProveedor))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(this);
        this.setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
    }// </editor-fold>//GEN-END:initComponents

    private void btnGuardarProveedorActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnGuardarProveedorActionPerformed
        if (validarDatos() == false) {
            JOptionPane.showMessageDialog(null, "Falta ingresar datos");
            return;
        }
        agregarProveedor();
        Window window = SwingUtilities.getWindowAncestor(this);
        if (window instanceof JDialog) {
            JDialog dialog = (JDialog) window;
            dialog.dispose();
        }
    }//GEN-LAST:event_btnGuardarProveedorActionPerformed

    private void btnActualizarProveedorActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnActualizarProveedorActionPerformed
        ActualizarProveedor();
        Window window = SwingUtilities.getWindowAncestor(this);
        if (window instanceof JDialog) {
            JDialog dialog = (JDialog) window;
            dialog.dispose();
        }
        btnGuardarProveedor.setEnabled(false);
    }//GEN-LAST:event_btnActualizarProveedorActionPerformed

    public void agregarProveedor() {
        String rucProv = txtRucProveedor.getText();
        String nomProv = txtNombreProveedor.getText();
        String celProv = txtCelularProveedor.getText();
        boolean esProv = chkActivoProveedor.isSelected();

        prove.setRucProveedor(rucProv);
        prove.setNombreProveedor(nomProv);
        prove.setCelularProveedor(celProv);
        prove.setEstadoProveedor(esProv);

        int respuesta = daoProveedor.agregarProve(prove);
        if (respuesta == 1) {
            JOptionPane.showMessageDialog(null, "Proveedor agregado con éxito");
        } else {
            JOptionPane.showMessageDialog(null, "Error");
        }
    }

    public void ActualizarProveedor() {
        String rucProv = txtRucProveedor.getText();
        String nomProv = txtNombreProveedor.getText();
        String celProv = txtCelularProveedor.getText();
        boolean esProv = chkActivoProveedor.isSelected();
        prove.setRucProveedor(rucProv);
        prove.setNombreProveedor(nomProv);
        prove.setCelularProveedor(celProv);
        prove.setEstadoProveedor(esProv);
        prove.setIdProveedor(Integer.valueOf(this.txtIdProveedor.getText()));
        int r = daoProveedor.actualizarProveedor(prove);
        if (r == 1) {
            JOptionPane.showMessageDialog(null, "Proveedor Actualizado con éxito");
        } else {
            JOptionPane.showMessageDialog(null, "Error al actualizar Proveedor");
        }
        btnGuardarProveedor.setEnabled(false);
    }

    private boolean validarDatos() {
        if (txtRucProveedor.getText().isEmpty()) {
            return false;
        }
        if (txtNombreProveedor.getText().isEmpty()) {
            return false;
        }
        if (txtCelularProveedor.getText().isEmpty()) {
            return false;
        }
        return true;
    }
    
    private void ValidarCampo() {
        // Validar campo de RUC
        ((AbstractDocument) txtRucProveedor.getDocument()).setDocumentFilter(new DocumentFilter() {
            public void insertString(DocumentFilter.FilterBypass fb, int offset, String text, AttributeSet attr)
                    throws BadLocationException {
                StringBuilder sb = new StringBuilder();
                sb.append(fb.getDocument().getText(0, fb.getDocument().getLength()));
                sb.insert(offset, text);

                if (sb.toString().matches("\\d{0,11}")) {
                    super.insertString(fb, offset, text, attr);
                }
            }

            @Override
            public void replace(DocumentFilter.FilterBypass fb, int offset, int length, String text, AttributeSet attrs)
                    throws BadLocationException {
                StringBuilder sb = new StringBuilder();
                sb.append(fb.getDocument().getText(0, fb.getDocument().getLength()));
                sb.replace(offset, offset + length, text);

                if (sb.toString().matches("\\d{0,11}")) {
                    super.replace(fb, offset, length, text, attrs);
                }
            }
        });

        // Validar campo de nombre
        ((AbstractDocument) txtNombreProveedor.getDocument()).setDocumentFilter(new DocumentFilter() {
            public void insertString(DocumentFilter.FilterBypass fb, int offset, String text, AttributeSet attr)
                    throws BadLocationException {
                StringBuilder sb = new StringBuilder();
                sb.append(fb.getDocument().getText(0, fb.getDocument().getLength()));
                sb.insert(offset, text);

                if (sb.toString().matches("[a-zA-Z ]{0,20}")) {
                    super.insertString(fb, offset, text, attr);
                }
            }

            @Override
            public void replace(DocumentFilter.FilterBypass fb, int offset, int length, String text, AttributeSet attrs)
                    throws BadLocationException {
                StringBuilder sb = new StringBuilder();
                sb.append(fb.getDocument().getText(0, fb.getDocument().getLength()));
                sb.replace(offset, offset + length, text);

                if (sb.toString().matches("[a-zA-Z ]{0,20}")) {
                    super.replace(fb, offset, length, text, attrs);
                }
            }
        });

        // Validar campo de celular
        ((AbstractDocument) txtCelularProveedor.getDocument()).setDocumentFilter(new DocumentFilter() {
            public void insertString(DocumentFilter.FilterBypass fb, int offset, String text, AttributeSet attr)
                    throws BadLocationException {
                StringBuilder sb = new StringBuilder();
                sb.append(fb.getDocument().getText(0, fb.getDocument().getLength()));
                sb.insert(offset, text);

                if (sb.toString().matches("\\d{0,9}")) {
                    super.insertString(fb, offset, text, attr);
                }
            }

            @Override
            public void replace(DocumentFilter.FilterBypass fb, int offset, int length, String text, AttributeSet attrs)
                    throws BadLocationException {
                StringBuilder sb = new StringBuilder();
                sb.append(fb.getDocument().getText(0, fb.getDocument().getLength()));
                sb.replace(offset, offset + length, text);

                if (sb.toString().matches("\\d{0,9}")) {
                    super.replace(fb, offset, length, text, attrs);
                }
            }
        });
    }

    public void setDatosEditar(Proveedor pr) {
        txtRucProveedor.setText(pr.getRucProveedor());
        txtNombreProveedor.setText(pr.getNombreProveedor());
        txtCelularProveedor.setText(pr.getCelularProveedor());
        chkActivoProveedor.setSelected(pr.isEstadoProveedor());
        txtIdProveedor.setText(Integer.toString(pr.getIdProveedor()));
        txtIdProveedor.setVisible(false);
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    public javax.swing.JButton btnActualizarProveedor;
    public javax.swing.JButton btnGuardarProveedor;
    public javax.swing.JCheckBox chkActivoProveedor;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JPanel jPanel1;
    public javax.swing.JPanel jPanel2;
    public javax.swing.JTextField txtCelularProveedor;
    private javax.swing.JLabel txtIdProveedor;
    public javax.swing.JTextField txtNombreProveedor;
    public javax.swing.JTextField txtRucProveedor;
    // End of variables declaration//GEN-END:variables
}

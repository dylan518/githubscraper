package poo.view.ProductosPorProveedor;

import poo.controller.ControllerGestion;
import poo.controller.ControllerGestion.*;
import poo.model.ProductoPorProveedor;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;


public class VistaProductosPorProveedor extends JFrame{
    private JTextField idProductoField;
    private JTextArea resultadoArea;

    public VistaProductosPorProveedor() {
        setTitle("Productos por Proveedor");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(475, 475);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        JLabel idProductoLabel = new JLabel("Ingrese ID de Producto:");
        idProductoField = new JTextField();
        JButton buscarButton = new JButton("Buscar");
        buscarButton.setForeground(Color.WHITE);
        buscarButton.setBackground(Color.BLUE);
        resultadoArea = new JTextArea(10, 10);
        resultadoArea.setEditable(false);

        JButton closeButton = new JButton("Cerrar");
        closeButton.setForeground(Color.WHITE);
        closeButton.setBackground(Color.RED);
        closeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Close the window when the close button is clicked
                dispose();
            }
        });

        buscarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                buscarProductosPorProveedor();
            }
        });

        panel.add(idProductoLabel);
        panel.add(idProductoField);
        panel.add(buscarButton);
        panel.add(new JScrollPane(resultadoArea));
        panel.add(closeButton);

        add(panel);
    }

    private void buscarProductosPorProveedor() {
        try {
            int idProducto = Integer.parseInt(idProductoField.getText());

            List<ProductoPorProveedor> productoPorProveedores = ControllerGestion.getControlador().obtenerProductosPorProveedorYProducto(idProducto);

            // Mostrar resultados en el JTextArea
            resultadoArea.setText("");
            if (!productoPorProveedores.isEmpty()) {
                resultadoArea.append("Proveedores para el Producto con ID " + idProducto + ":\n");
                for (ProductoPorProveedor productoPorProveedor : productoPorProveedores) {
                    resultadoArea.append("Proveedor:  " + productoPorProveedor.getProveedor().getNombre() + " - CUIT:  " + productoPorProveedor.getProveedor().getCuit() + " - Producto:  " + productoPorProveedor.getProducto().getNombreProducto() + " - Precio:  " + productoPorProveedor.getUltimoPrecio() +"\n");
                }

            } else {
                resultadoArea.append("No se encontraron proveedores para el Producto con ID " + idProducto);
            }

        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Ingrese un ID de producto válido.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

}




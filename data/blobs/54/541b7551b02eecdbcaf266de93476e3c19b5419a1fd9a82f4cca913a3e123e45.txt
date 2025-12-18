import javax.swing.*;
import javax.swing.event.*;
import java.awt.*;
import java.awt.event.*;

public class MainWindow extends JFrame {
    private JLabel mainHeading;
    private JButton addCustomerButton;
    private JButton placeOrderButton;
    private JButton viewOrderButton;
    private JButton updateOrderButton;
    private AddCustomerForm addCustomerForm;
    private PlaceOrder placeOrder;
    private ViewOrder viewOrder;
    private UpdateOrder updateOrder;

    public MainWindow() {
        setSize(600, 600);
        setTitle("iBurgerShop Management System");
        setResizable(false);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);




        JPanel headingPanel = new JPanel();


        mainHeading = new JLabel("iBurger Shop");
        mainHeading.setFont(new Font("MV Boli", 1, 45));

        ImageIcon image =new ImageIcon("logo5.png");
        mainHeading.setIcon(image);



        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(null);
        mainPanel.setBackground(new Color(203, 228, 222));
        JPanel centerPanel = new JPanel(new GridLayout(4, 1, 20, 20));
        centerPanel.setBounds(100, 45, 400, 300);
        centerPanel.setBackground(new Color(203, 228, 222));

        addCustomerForm = new AddCustomerForm();

        addCustomerButton = new JButton();
        addCustomerButton.setText("Add Customer");
        addCustomerButton.setFocusable(false);
        addCustomerButton.setFont(new Font("", 1, 25));
        addCustomerButton.setBackground(new Color(44, 51, 51));
        addCustomerButton.setForeground(new Color(255, 255, 255));
        addCustomerButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                dispose();
                addCustomerForm.setVisible(true);
            }
        });


        placeOrder = new PlaceOrder();

        placeOrderButton = new JButton();
        placeOrderButton.setText("Place Order");
        placeOrderButton.setFocusable(false);
        placeOrderButton.setFont(new Font("", 1, 25));
        placeOrderButton.setBackground(new Color(44, 51, 51));
        placeOrderButton.setForeground(new Color(255, 255, 255));
        placeOrderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                dispose();
                placeOrder.setVisible(true);
            }
        });

        viewOrder = new ViewOrder();
        viewOrderButton = new JButton();
        viewOrderButton.setText("View Orders");
        viewOrderButton.setFocusable(false);
        viewOrderButton.setFont(new Font("", 1, 25));
        viewOrderButton.setBackground(new Color(44, 51, 51));
        viewOrderButton.setForeground(new Color(255, 255, 255));
        viewOrderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                dispose();
                viewOrder.setVisible(true);
            }
        });



        updateOrder = new UpdateOrder();
        updateOrderButton = new JButton();
        updateOrderButton.setText("Update Order Details");
        updateOrderButton.setFocusable(false);
        updateOrderButton.setFont(new Font("", 1, 25));
        updateOrderButton.setBackground(new Color(44, 51, 51));
        updateOrderButton.setForeground(new Color(255, 255, 255));
        updateOrderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                dispose();
                updateOrder.setVisible(true);
            }
        });

        centerPanel.add(addCustomerButton);
        centerPanel.add(placeOrderButton);
        centerPanel.add(viewOrderButton);
        centerPanel.add(updateOrderButton);

        headingPanel.add(mainHeading);
        mainPanel.add(centerPanel);

        add("North", headingPanel);
        add("Center", mainPanel);



    }
}

package org.example.view;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;
import java.sql.Date;

public class ReservationView {
    private JTextField beginDayField;
    private JTextField beginMonthField;
    private JTextField beginYearField;
    private JTextField endDayField;
    private JTextField endMonthField;
    private JTextField endYearField;
    private JButton reserveButton;

    public ReservationView() {
        // Initialize components
        beginDayField = new JTextField();
        beginMonthField = new JTextField();
        beginYearField = new JTextField();
        endDayField = new JTextField();
        endMonthField = new JTextField();
        endYearField = new JTextField();
        reserveButton = new JButton("Reserve");

        // Set layout and add components
        JPanel panel = new JPanel(new GridLayout(7, 2));
        panel.add(new JLabel("Begin Date - Day:"));
        panel.add(beginDayField);
        panel.add(new JLabel("Begin Date - Month:"));
        panel.add(beginMonthField);
        panel.add(new JLabel("Begin Date - Year:"));
        panel.add(beginYearField);
        panel.add(new JLabel("End Date - Day:"));
        panel.add(endDayField);
        panel.add(new JLabel("End Date - Month:"));
        panel.add(endMonthField);
        panel.add(new JLabel("End Date - Year:"));
        panel.add(endYearField);
        panel.add(new JLabel()); // Placeholder for spacing
        panel.add(reserveButton);

        // Create a frame and add the panel to it
        JFrame frame = new JFrame("Client View");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(panel);
        frame.pack();
        frame.setVisible(true);
    }

    // Method to get the begin date entered by the user
    public Date getBeginDate() {
        // Parse the text fields to get day, month, and year
        int beginDay = Integer.parseInt(beginDayField.getText());
        int beginMonth = Integer.parseInt(beginMonthField.getText());
        int beginYear = Integer.parseInt(beginYearField.getText());

        // Create a java.sql.Date object
        return new Date(beginYear - 1900, beginMonth - 1, beginDay);
    }

    // Method to get the end date entered by the user
    public Date getEndDate() {
        // Parse the text fields to get day, month, and year
        int endDay = Integer.parseInt(endDayField.getText());
        int endMonth = Integer.parseInt(endMonthField.getText());
        int endYear = Integer.parseInt(endYearField.getText());

        // Create a java.sql.Date object
        return new Date(endYear - 1900, endMonth - 1, endDay);


    }

    // Method to set action listener for reserve button
    public void onReserveButtonClicked(ActionListener listener) {
        reserveButton.addActionListener(listener);
    }

    // Method to display a message to the user
    public void showMessage(String message) {
        JOptionPane.showMessageDialog(null, message);
    }
}


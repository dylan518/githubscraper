package cz.michal.reader;

import javax.swing.*;
import java.io.File;
import java.util.List;

public class GUI extends JFrame {

    private JButton openFile;
    private JTextArea data;
    private JPanel panel;

    private final JFileChooser jFileChooser = new JFileChooser(".");

    public GUI() {
        openFile.addActionListener(e -> showFileChooser());
        initComponents();
    }

    private void showFileChooser() {
        int result = jFileChooser.showOpenDialog(this);

        if (result == JFileChooser.ERROR_OPTION) {
            JOptionPane.showMessageDialog(null, "Invalid option, please select file again!");
            return;
        }

        System.out.println("Reading..");
        loadData(jFileChooser.getSelectedFile());
    }

    private void loadData(File file) {
        clearData();

        List<String> listData = FileUtils.readData(file);

        if (listData == null) {
            JOptionPane.showMessageDialog(null, "Invalid option, please select file again!");
            return;
        }

        if (listData.isEmpty()) {
            JOptionPane.showMessageDialog(null, "File is empty!");
            return;
        }

        listData.forEach(s -> data.append(s + "\n"));
    }

    private void clearData() {
        data.setText(null);
    }

    private void initComponents() {
        JMenuBar jMenuBar = new JMenuBar();

        JMenu menu = new JMenu("File");

        JMenuItem openItem = new JMenuItem("Open");
        openItem.addActionListener(e -> showFileChooser());

        menu.add(openItem);
        menu.addSeparator();

        JMenuItem clearData = new JMenuItem("Clear");
        clearData.addActionListener(e -> clearData());

        menu.add(clearData);

        jMenuBar.add(menu);
        setJMenuBar(jMenuBar);

        data.setEditable(false);
    }

    public static void main(String[] args) {
        GUI gui = new GUI();
        gui.setContentPane(gui.panel);
        gui.setDefaultCloseOperation(EXIT_ON_CLOSE);
        gui.setSize(500, 500);
        gui.setVisible(true);
    }
}

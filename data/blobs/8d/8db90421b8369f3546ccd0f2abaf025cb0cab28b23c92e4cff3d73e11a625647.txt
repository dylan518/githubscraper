package gui;

import javax.swing.*;
import java.awt.event.ActionListener;

public class Root {
    //Паттерн одиночка
    private static Boolean instance = false;

    private JFrame root;

    public JFrame getWindow() {
        return root;
    }

    public Root(String title, Integer width, Integer height) {
        if (instance) {
            try {
                throw new Exception("Главное окно уже создано");
            } catch (Exception e) {
                System.out.println("Главное окно уже создано!");

            }
        } else {
            instance = true;
            root = new JFrame(title);
            root.setSize(width, height);
        }
    }

    public void Run() {
            root.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            root.setVisible(true);
        }

    public JPanel addPanel() {
        JPanel panel = new JPanel();
        root.add(panel);
        return panel;
    }

    public JButton addButton(JPanel container, String text) {
        JButton button = new JButton(text);
        container.add(button);
        return button;
    }

    public JButton addButton(JPanel container, String text, ActionListener listener) {
        JButton button = new JButton(text);

        //Обработчик события
        button.addActionListener(listener);

        container.add(button);
        return button;
    }
}



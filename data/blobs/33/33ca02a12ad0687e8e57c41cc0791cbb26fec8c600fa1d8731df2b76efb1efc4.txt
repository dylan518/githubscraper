import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Calc implements ActionListener {
    JFrame jFrame;
    JTextField jTextField;
    JButton[] numButtons = new JButton[10];
    JButton[] funcButtons = new JButton[8];
    JButton addButt, subButt, mulButt, divButt;
    JButton decButt, equalButt, delButt, clearButt;
    JPanel jPanel;

    Font font = new Font("serif",Font.PLAIN,20);
    double num1 = 0, num2 = 0, result = 0;
    char op;

    Calc(){
        jFrame = new JFrame();
        jFrame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        jFrame.setSize(350,500);
        jFrame.setTitle("CALCULATOR");
        jFrame.setLayout(null);
        jFrame.setResizable(false);
        jFrame.setLocationRelativeTo(null);

        jTextField = new JTextField();
        jTextField.setBounds(20,20,300,50);
        jTextField.setFont(font);
        jTextField.setEditable(false);

        addButt = new JButton("+");
        subButt = new JButton("-");
        mulButt = new JButton("*");
        divButt = new JButton("/");
        decButt = new JButton(".");
        equalButt = new JButton("=");
        delButt = new JButton("Delete");
        clearButt = new JButton("Clear");

        funcButtons[0] = addButt;
        funcButtons[1] = subButt;
        funcButtons[2] = mulButt;
        funcButtons[3] = divButt;
        funcButtons[4] = decButt;
        funcButtons[5] = equalButt;
        funcButtons[6] = delButt;
        funcButtons[7] = clearButt;

        for (int i = 0; i <8 ; i++) {
            funcButtons[i].addActionListener(this);
            funcButtons[i].setFont(font);
            funcButtons[i].setFocusable(false);
        }

        for (int i = 0; i <10 ; i++) {
            numButtons[i] = new JButton(String.valueOf(i));
            numButtons[i].addActionListener(this);
            numButtons[i].setFont(font);
            numButtons[i].setFocusable(false);
        }

        delButt.setBounds(40,400,100,40);
        clearButt.setBounds(200,400,100,40);

        jPanel = new JPanel();
        jPanel.setBounds(20,90,300,300);
        jPanel.setLayout(new GridLayout(4,4,10,10));
        jPanel.setBackground(new Color(142, 237, 168));

        jPanel.add(numButtons[1]);
        jPanel.add(numButtons[2]);
        jPanel.add(numButtons[3]);
        jPanel.add(addButt);
        jPanel.add(numButtons[4]);
        jPanel.add(numButtons[5]);
        jPanel.add(numButtons[6]);
        jPanel.add(subButt);
        jPanel.add(numButtons[7]);
        jPanel.add(numButtons[8]);
        jPanel.add(numButtons[9]);
        jPanel.add(mulButt);
        jPanel.add(decButt);
        jPanel.add(numButtons[0]);
        jPanel.add(equalButt);
        jPanel.add(divButt);


        jFrame.add(jPanel);
        jFrame.add(delButt);
        jFrame.add(clearButt);
        jFrame.add(jTextField);
        jFrame.setVisible(true);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        for (int i = 0; i <10 ; i++) {
            if (e.getSource()==numButtons[i]){
                jTextField.setText(jTextField.getText().concat(String.valueOf(i)));
            }
        }
        if (e.getSource()==decButt){
            jTextField.setText(jTextField.getText().concat("."));
        }
        if (e.getSource()==addButt){
            num1 = Double.parseDouble(jTextField.getText());
            op = '+';
            jTextField.setText("");

        }
        if (e.getSource()==subButt){
            num1 = Double.parseDouble(jTextField.getText());
            op = '-';
            jTextField.setText("");

        }
        if (e.getSource()==mulButt){
            num1 = Double.parseDouble(jTextField.getText());
            op = '*';
            jTextField.setText("");

        }
        if (e.getSource()==divButt){
            num1 = Double.parseDouble(jTextField.getText());
            op = '/';
            jTextField.setText("");

        }
        if (e.getSource()==equalButt){
            num2 = Double.parseDouble(jTextField.getText());

            switch (op){
                case '+':
                    result = num1 + num2;
                    break;
                case '-':
                    result = num1 - num2;
                    break;
                case '*':
                    result = num1 * num2;
                    break;
                case '/':
                    result = num1 / num2;
                    break;
            }
            jTextField.setText(String.valueOf(result));
            num1 = result;
        }
        if (e.getSource()==clearButt){
            jTextField.setText("");
        }
        if (e.getSource()==delButt){
            String str = jTextField.getText();
            jTextField.setText("");
            for (int i = 0; i < str.length() - 1; i++) {
                jTextField.setText(jTextField.getText() + str.charAt(i));

            }
        }

    }
}

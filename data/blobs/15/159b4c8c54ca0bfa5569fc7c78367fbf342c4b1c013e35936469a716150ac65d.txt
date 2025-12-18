import javax.swing.*;
import java.awt.event.*;

public class MainGUIWindow extends JFrame implements ActionListener {
    private JPanel mainPanel;
    private JTextArea billTextArea;
    private JTextArea tipTextArea;
    private JLabel Bill;
    private JLabel Tip;
    private JLabel totalTipLabel;
    private JTextArea numberOfPeopleTextArea;
    private JLabel totalBillLabel;
    private JLabel numberOfPeopleLabel;
    private JButton incrementTip;
    private JButton decrementTip;
    private JButton incrementPeople;
    private JButton decrementPeople;
    private JTextPane totalTipPane;
    private JTextPane totalBillPane;
    private JButton submitButton;

    public MainGUIWindow(){
        createUIComponents();
    }

    private void createUIComponents() {
        setContentPane(mainPanel);
        setTitle("My Tip Calculator GUI!");
        setSize(700,700);
        setLocation(450,100);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        incrementTip.addActionListener(this);
        decrementTip.addActionListener(this);
        incrementPeople.addActionListener(this);
        decrementPeople.addActionListener(this);
        submitButton.addActionListener(this);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e){
        Object source = e.getSource();
        if (source instanceof JButton){
            JButton button = (JButton) source;
            if(button.getText().equals("- %")){
                int current = Integer.parseInt(tipTextArea.getText());
                tipTextArea.setText("" + (current-1));
            } else if (button.getText().equals("+ %")){
                int current = Integer.parseInt(tipTextArea.getText());
                tipTextArea.setText("" + (current+1));
            } else if (button.getText().equals("-") && !numberOfPeopleTextArea.getText().equals("1")){
                int current = Integer.parseInt(numberOfPeopleTextArea.getText());
                numberOfPeopleTextArea.setText("" + (current-1));
            } else if (button.getText().equals("+")){
                int current = Integer.parseInt(numberOfPeopleTextArea.getText());
                numberOfPeopleTextArea.setText("" + (current+1));
            } else {
                if(Integer.parseInt(numberOfPeopleTextArea.getText()) == 1){
                    TipCalculator run = new TipCalculator(Integer.parseInt(billTextArea.getText()), Integer.parseInt(tipTextArea.getText()), Integer.parseInt(numberOfPeopleTextArea.getText()));
                    if(Integer.parseInt(billTextArea.getText())!=0){
                        totalTipLabel.setText("Total Tip");
                        totalTipPane.setText("" + run.calculateTip());
                        totalBillLabel.setText("Total Bill");
                        totalBillPane.setText("" + run.totalBill());
                    }
                } else {
                    TipCalculator run = new TipCalculator(Integer.parseInt(billTextArea.getText()), Integer.parseInt(tipTextArea.getText()), Integer.parseInt(numberOfPeopleTextArea.getText()));
                    if (Integer.parseInt(billTextArea.getText())!=0){
                        totalTipLabel.setText("Total Tip per Person");
                        totalTipPane.setText("" + run.tipPerPerson());
                        totalBillLabel.setText("Total per Person");
                        totalBillPane.setText("" + run.totalPerPerson());
                    }
                }

            }
        }

    }
}

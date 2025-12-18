package course.management.system;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.border.*;

public class ChooseReport extends JFrame implements ActionListener{

    private JPanel contentPane;
    private JButton b1,b2;
    private JButton b3;

    public static void main(String[] args) {
        new ChooseReport().setVisible(true);
    }

    public ChooseReport() {

        setBounds(400, 150, 725, 525);
        contentPane = new JPanel();
        setContentPane(contentPane);
        contentPane.setLayout(null);
        contentPane.setBackground(new Color(204, 204, 255));


        JMenuBar menuBar = new JMenuBar();
        menuBar.setBorder(new EtchedBorder(EtchedBorder.LOWERED, new Color(0, 0, 0), new Color(0, 0, 0)));
        menuBar.setBackground(new Color(204, 204, 255));
        menuBar.setBounds(0, 10, 1000, 35);
        contentPane.add(menuBar);

        JMenu mnExit = new JMenu("Exit");
        mnExit.setForeground(Color.BLACK);
        mnExit.setFont(new Font("Trebuchet MS", Font.BOLD, 17));


        JMenuItem mntmLogout = new JMenuItem("Logout");
        mntmLogout.setBackground(new Color(211, 211, 211));
        mntmLogout.setForeground(new Color(105, 105, 105));
        mntmLogout.addActionListener(this);
        mnExit.add(mntmLogout);

        JMenuItem mntmExit = new JMenuItem("Exit");
        mntmExit.setForeground(new Color(105, 105, 105));
        mntmExit.setBackground(new Color(211, 211, 211));
        mntmExit.addActionListener(this);
        mnExit.add(mntmExit);
        menuBar.add(mnExit);

        JLabel l1 = new JLabel("Admin Dashboard");
        l1.setForeground(new Color(0, 0, 0));
        l1.setFont(new Font("Segoe UI Semilight", Font.BOLD, 30));
        l1.setBounds(240, 30, 328, 80);
        contentPane.add(l1);

        JPanel panel = new JPanel();
        panel.setBorder(new TitledBorder(new LineBorder(new Color(0, 0, 0), 2), "Works", TitledBorder.LEADING, TitledBorder.TOP, null, new Color(0, 0, 0)));
        panel.setBounds(122, 107, 491, 355);
        panel.setBackground(new Color(204, 204, 255));
        contentPane.add(panel);
        panel.setLayout(null);
        
        b2 = new JButton("Level 5");
        b2.setBounds(137, 148, 200, 76);
        panel.add(b2);
        b2.addActionListener(this);
        b2.setBackground(new Color(0, 0, 102));
        b2.setForeground(Color.WHITE);
        
        
        b1 = new JButton("Level 4");
        b1.setBounds(137, 51, 200, 76);
        panel.add(b1);
        b1.addActionListener(this);
        b1.setBackground(new Color(0, 0, 102));
        b1.setForeground(Color.WHITE);
        
        JLabel l2 = new JLabel("<--");
        l2.setBounds(22, 24, 72, 33);
        panel.add(l2);
        l2.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                setVisible(false);
                AdminHome home = new AdminHome();
                home.setVisible(true);
            }
        });
        l2.setForeground(Color.BLACK);
        l2.setFont(new Font("Trebuchet MS", Font.BOLD, 25));
        
        b3 = new JButton("Level 6");
        b3.setForeground(Color.WHITE);
        b3.setBackground(new Color(0, 0, 102));
        b3.setBounds(137, 251, 200, 76);
        panel.add(b3);
        b3.addActionListener(this);
    }
    
    public void actionPerformed(ActionEvent ae){
        String msg = ae.getActionCommand();
        if(msg.equals("Logout")){
            setVisible(false);
            new Main().setVisible(true);
        }else if(msg.equals("Exit")){
            System.exit(ABORT);
        }
        if(ae.getSource() == b1){
            this.setVisible(false);
            new GenerateReport().setVisible(true);
        }
        if(ae.getSource() == b2){
            this.setVisible(false);
            new GenerateReport1().setVisible(true);
        }
        if(ae.getSource() == b3){
            this.setVisible(false);
            new GenerateReport2().setVisible(true);
        }
    }
}

import javax.swing.*;
import java.awt.*;

public class Panel extends JFrame {
    public Panel(){
        this.setTitle("Windows Testing");
        this.setSize(600,500); // dimensions of a this.
        this.setResizable(false); // used by organization so that layout won't be affected.
        this.setVisible(true); // letting our this visible on the screen.

        ImageIcon icon = new ImageIcon("icon.png"); // initialize icon object
        this.setIconImage(icon.getImage()); // changes icon of our window
        this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
//        this.getContentPane().setBackground(new Color(68, 68, 68));

        this.getContentPane().setCursor(new Cursor(1));

    }

}

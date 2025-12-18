package ElementAdding;

import java.awt.*;

public class ButtonLabelTextfield extends Frame {
    Button b1, b2;
    Label l1, l2, l3, l4;
    TextField t1, t2;

    ButtonLabelTextfield() {
        // GridLayout is the style in which the element will be get arranged
        GridLayout g = new GridLayout(4, 2);
        setLayout(g);
        b1 = new Button(" Press OK");
        b2 = new Button("Cancel");
        l1 = new Label("Name");
        l2 = new Label("Mobile Number");
        l3 = new Label("Age");
        l4 = new Label("Adress");
        t1 = new TextField("Text1");
        t2 = new TextField("Test2");
        add(b1);
        add(b2);
        add(l1);
        add(l2);
        add(l3);
        add(l4);
        add(t1);
        add(t2);
    }

    public static void main(String[] args) {
        ButtonLabelTextfield x = new ButtonLabelTextfield();
        x.setSize(1000, 700);
        x.setVisible(true);
    }
}

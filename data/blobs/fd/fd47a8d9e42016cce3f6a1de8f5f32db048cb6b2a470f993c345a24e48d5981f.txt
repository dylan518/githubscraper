package it.unitn.disi.prog2.aliprandi.myproject.Controllers;

import it.unitn.disi.prog2.aliprandi.myproject.JavaFX.BlockPane;
import it.unitn.disi.prog2.aliprandi.myproject.JavaFX.FurnacePane;
import it.unitn.disi.prog2.aliprandi.myproject.JavaFX.InternalListener;
import it.unitn.disi.prog2.aliprandi.myproject.data.*;
import it.unitn.disi.prog2.aliprandi.myproject.interfaces.SimpleController;
import it.unitn.disi.prog2.aliprandi.myproject.interfaces.SmeltableBlock;
import javafx.scene.Node;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;

import java.util.List;
import java.util.ListIterator;

public class FurnaceController implements SimpleController {

    public Furnace furnace;
    public FurnacePane furnacePane;
    private MainController mc;

    public FurnaceController(Furnace furnace, FurnacePane furnacePane, MainController mc) {
        this.furnace = furnace;
        this.furnacePane=furnacePane;

        this.mc=mc;

        redraw();
    }

    @Override
    public void redraw() {

        List<Node> children = this.furnacePane.getChildren();
        ListIterator<Node> iterator = children.listIterator();

        while (iterator.hasNext()) {
            Node x = iterator.next();
            iterator.remove();
        }

        children.add(new Text("Furnace"));
        children.add(new InternalListener(this.furnace.getInput(),this.mc,"input"));
        children.add(new Text("--->"));
        HBox h  = new HBox();
        InternalListener i = new InternalListener(this.furnace.getFuel(),this.mc,"fuel");
        Text t = new Text(""+this.furnace.getFuelLevel());
        t.setFill(Color.WHITE);
        i.getChildren().add(t);
        h.getChildren().add(i);
        h.getChildren().add(new InternalListener(this.furnace.getOutput(),this.mc, "output"));
        children.add(h);

        //this.furnace.display();

    }

}

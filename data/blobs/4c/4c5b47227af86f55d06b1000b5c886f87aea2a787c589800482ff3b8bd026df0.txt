// import java.awt.*;
import java.util.ArrayList;
// import java.util.HashMap;
import java.util.List;
// import java.util.Map;

public class Notebook {

    private String Name;

    private int OpRAM;
    private String OpSystem;
    private int Price;
    private String Model;

    public Notebook(String Name, int OpRAM, String OpSystem, int Price, String Model) {
        this.Name = Name;
        this.OpRAM = OpRAM;
        this.OpSystem = OpSystem;
        this.Price = Price;
        this.Model = Model;
    }

    public boolean validateObject(){
        return true;
    }

    public static List<String> propertiesForFilter(){
        List<String> list = new ArrayList<>();
        list.add("OpRAM");
        list.add("OpSystem");
        list.add("Price");
        list.add("Model");

        return list;

    }

    @Override
    public String toString() {
        return "Ноутбук: (" + Name + ")  " +
                "Оперативная память: " + OpRAM +
                ", Операционная система: " + OpSystem + 
                ", Цена: " + Price +
                ", Модель: " + Model;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public int getOpRAM() {
        return OpRAM;
    }

    public void setRAM(int amountRAM) {
        this.OpRAM = OpRAM;
    }

    public String getOpSystem() {
        return OpSystem;
    }

    public void setOpSystem(String OpSystem) {
        this.OpSystem = OpSystem;
    }

    public int getPrice() {
        return Price;
    }

    public void setPrice(int Price) {
        this.Price = Price;
    }

    public String getModel() {
        return Model;
    }

    public void setModel(String Model) {
        this.Model = Model;
    }
}
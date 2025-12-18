package model;

import db.objects.Supplier;
import db.use.Model;
import java.util.ArrayList;

public class SuppliersModel extends Model {
    public SuppliersModel() {
        super("Suppliers", 6);
    }
    
    public static ArrayList<Supplier> takeObject(ArrayList<String[]> listArr) {
        ArrayList<Supplier> result = new ArrayList<>();
        for (int i = 0; i < listArr.size(); i++) {
            result.add(new Supplier(listArr.get(i)));
        }
        return result;
    }
}

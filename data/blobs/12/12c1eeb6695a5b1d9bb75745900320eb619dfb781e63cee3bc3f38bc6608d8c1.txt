import java.util.ArrayList;
import java.util.Random;

public abstract class RegroupementHumain {

    ArrayList<Humains> leRegroupement = new ArrayList<Humains>();
    Humains chef;

    public RegroupementHumain(Humains chef) {
        this.chef = chef;
    }

    public abstract ArrayList<Humains> justLesBagarreurs();

    public abstract String seRencontrer(Humains h1, Humains h2);

    public void addHumain(Humains h) {
        leRegroupement.add(h);
    }

    public ArrayList<Humains> getLeRegroupement() {
        return leRegroupement;
    }
}

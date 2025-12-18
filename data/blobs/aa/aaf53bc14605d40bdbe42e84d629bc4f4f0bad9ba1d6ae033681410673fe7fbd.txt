import java.util.ArrayList;

public class Tier {
    public static ArrayList <Tier> tiere = new ArrayList<>();

    private int unterhalt;

    public Tier(int unterhalt) {
        this.unterhalt = unterhalt;
        tiere.add(this);
        for (Produkt produkt : Produkt.produkte) {
            produkt.updateProdukt(this);
        }
    }

        public int getUnterhalt () {
            return unterhalt;
        }
    }

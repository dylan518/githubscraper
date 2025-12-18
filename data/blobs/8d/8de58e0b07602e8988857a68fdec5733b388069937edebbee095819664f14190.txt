import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Cereal> cList = new ArrayList<Cereal>();

        //Cereal test = new Cereal("test", 100);
        Cereal Bran = new Cereal("100% Bran", 70);
        Cereal naturalBran = new Cereal("100% Natural Bran", 120);
        Cereal all_Bran = new Cereal("All-Bran", 70);
        Cereal all_Bran_Fiber = new Cereal("All-Bran with Extra Fiber", 50);
        Cereal almondDelight = new Cereal("Almond Delight", 110);
        Cereal appleCinnamon = new Cereal("Apple Cinnamon Cheerios", 110);

        cList.add(Bran);
        cList.add(naturalBran);
        cList.add(all_Bran);
        cList.add(all_Bran_Fiber);
        cList.add(almondDelight);
        cList.add(appleCinnamon);

        System.out.println(cList);

        int most = 0;
        int num = 0;
        for (int i = 0; i < cList.size(); i++) {
            if (cList.get(i).getCalories() > most) {
                most = cList.get(i).getCalories();
                num = i;
            }
        }
        System.out.println("The cereal with the most calories is " + cList.get(num).getName());
    }
}

package cicli;

import java.util.Random;

public class TestRandom {

    public static void main(String[] args) {
        double numero;
        int intero;
        
        Random r = new Random();

        for (int i = 0; i < 100000000; i++) {
            intero = r.nextInt(4)+1;
            System.out.println("numero :" + intero);
        }

    }

}

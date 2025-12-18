
import java.util.Arrays;


public class Main {
    public static void main(String[] args) {
        float [] begrenzung = new float [2];
        begrenzung[0] =0.5f;
        begrenzung[1] =0.7f;
        float ergebnis = begrenzteZufallsZahl(begrenzung);
        System.out.println(ergebnis);


        int[] intArray2 = new int[1000];
        for (int i =0; i<1000;i++){
            intArray2[i]= i+1;
        }
        System.out.println(Arrays.toString(intArray2));
        schleife();
    }
    public static float begrenzteZufallsZahl(float[] begrenzung){
        //generieren
        boolean gefunden =true;
        while (gefunden){


            float zufallsZahl = (float) Math.random();

            gefunden =false;
            // ist enthalten?
            for (int i = 0; i<begrenzung.length;i++){
                float schublade = begrenzung[i];
                // ja-> neue generieren
                if(zufallsZahl == schublade){
                    gefunden =true;
                }
            } //nein ->zurück geben
            if (gefunden ==false){
                return zufallsZahl;
            }
        }
        return  -1;
    }
    public static int schleife(){
        for (int i=3; i >=0 ;i--){
            System.out.println(i);
        }return 0 ;
    }
}

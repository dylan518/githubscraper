package mx.utng.s20;

public class Gobierno {
    private static Gobierno instance;

    private Gobierno(){
        System.out.println("Unica instancia de gobierno");
    }

    public static Gobierno getInstance(){
        if(instance == null){
            instance = new Gobierno();
        }
        return instance;
    }

    public void darApoyo(){
        System.out.println("Dando apoyo al ciudadano");
    }

}

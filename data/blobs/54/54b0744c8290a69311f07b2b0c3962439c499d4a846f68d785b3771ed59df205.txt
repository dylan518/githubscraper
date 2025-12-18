package Lambada;

import java.util.TreeSet;

public class ProvaLambda {

    public static void main(String[] args) {
        //creo oggetto comparatore una sola volta e lo utilizzo nel costruttore del treeset
        Comparatore comparatore = new Comparatore();
        TreeSet<String> parole = new TreeSet<>(comparatore);

        parole.add("java");
        parole.add("html");
        parole.add("css");
        parole.add("javascript");

        System.out.println(parole);
    }

}

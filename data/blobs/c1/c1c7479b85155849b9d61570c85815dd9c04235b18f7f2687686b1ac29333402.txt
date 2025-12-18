package Ex2;

import java.io.*;
import java.util.Scanner;

public class MainApp {
    public static void main(String[] args) throws IOException {
        //STRING TOKENIZER
        String pathName = "D:\\Facultate\\Anul III\\Semestrul I\\PJ\\Laborator\\Lab2\\src\\Ex2\\cantec_in.txt";
        BufferedReader br = new BufferedReader(new FileReader(pathName));

        String linie;
        Vers vers;
        int nrCuv, nrVoc;
        double rand;

        PrintStream printStream = new PrintStream("D:\\Facultate\\Anul III\\Semestrul I\\PJ\\Laborator\\Lab2\\src\\Ex2\\cantec_out.txt");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduceti o grupare de litere:");
        String grup = scanner.next();

        while ((linie = br.readLine()) != null) {
            vers = new Vers(linie);
            nrCuv = vers.getNrCuv();
            nrVoc = vers.getNrVoc();
            if (grup.compareTo(linie.substring(linie.length() - grup.length())) == 0) {
                linie += "*";
            }
            linie += " - " + nrCuv + " cuv si " + nrVoc + " vocale";
            rand = Math.random();
            if (rand < 0.1) {
                linie = linie.toUpperCase();
            }
            printStream.println(linie);
        }
        printStream.close();
    }
}

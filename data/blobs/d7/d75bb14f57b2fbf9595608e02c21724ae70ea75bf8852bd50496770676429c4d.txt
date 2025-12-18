import java.util.Scanner;

public class EX06_05 {
    public static void main(String[] args) throws InterruptedException {
        Scanner kyselija = new Scanner(System.in);
        String lause1 = lauseKyselija(kyselija);
        String lause2 = lauseKyselija(kyselija);

        pidempiLause(lause1, lause2);   
    }

    public static String lauseKyselija(Scanner kyselija) {
        System.out.println("Syötä lause");
        String lause1 = kyselija.nextLine();
        return lause1;
    }

    public static int laskeSanat(String lause) {
        int sanat = 0;
        Scanner sanaLaskija = new Scanner(lause);
        while (sanaLaskija.hasNext()) {
            sanat++;
            sanaLaskija.next();
        }
        sanaLaskija.close();
        return sanat;
    }

    public static void pidempiLause(String lause1, String lause2) {
        int lause1Pituus = laskeSanat(lause1);
        int lause2Pituus = laskeSanat(lause2);

        if(lause1Pituus > lause2Pituus) {
            System.out.println("Lause 1 on pidempi, siinä on " + lause1Pituus + " sanaa");
        } else if(lause2Pituus > lause1Pituus) {
            System.out.println("Lause 2 on pidempi, siinä on " + lause2Pituus + " sanaa");
        } else if(lause1Pituus == lause2Pituus) {
            System.out.println("Lauseet ovat yhtä pitkiä");
        }
    }
}
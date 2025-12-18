public class Calcule {
    public static Integer nombreDeChiffre(Integer nombre){
        int nombreDeChiffres = 0;

        while (nombre != 0) {
            nombre /= 10;
            nombreDeChiffres++;
        }
        return nombreDeChiffres -1;
    }

    public static Integer calcule(Integer nombre, Integer puissanceIni) {
        Integer somme = 0;
        int puissance = puissanceIni;

        while (nombre > 0) {
            Integer dernierChiffre = nombre % 10;

            Integer valeur = dernierChiffre * (int) Math.pow(10, puissance);

            somme += valeur;

            nombre = nombre / 10;

            puissance--;
        }

        return somme;
    }
    public static Integer somme(Integer nombre) {
        Integer puissance = nombreDeChiffre(nombre);
        Integer inverse = calcule(nombre, puissance);
        Integer somme = nombre + inverse;
        System.out.println( nombre + "+" + inverse + '='+somme);

        while (!somme.equals(calcule(somme, nombreDeChiffre(somme)))) {
            nombre = somme;
            inverse = calcule(nombre, nombreDeChiffre(nombre));
            somme = nombre + inverse;
            System.out.println( nombre + "+" + inverse + '='+somme);
        }

        return somme;
    }

}

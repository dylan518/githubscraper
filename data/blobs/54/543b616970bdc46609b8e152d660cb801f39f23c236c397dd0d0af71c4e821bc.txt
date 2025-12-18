import java.util.Scanner;
//6- Dibuixa el següent gràfic. Paràmetres: nombre de voltes de l'espiral i número de costats del
//polígon de base.


public class Exercici6 {
    public static void main(String[] args) {
        Turtle t = new Turtle(700, 700);
        Scanner scanner = new Scanner(System.in);

        System.out.println("Tamaño de los costados: ");
        int costados = scanner.nextInt();

        System.out.println("Numero de vueltas del poligono: ");
        int numeroVueltas = scanner.nextInt();

        System.out.println("Cuantos costados quieres que tenga el poligono: ");
        int poligonoCostados = scanner.nextInt();


        if (poligonoCostados <= 2) {
            System.out.println("No puedes añadir un poligono con menos de dos costados.");
        }

        for (int i = 0; i < numeroVueltas; i++) {
            poligono(t, costados, poligonoCostados);
            costados += 15;
        }



        //t.setDelay(500);
        t.markCursor();
        t.show();
    }


    public static void poligono(Turtle t, int costados, int poligonoCostados) {
        for (int i = 0; i < poligonoCostados / 2; i++) {
            t.forward(costados);
            t.turnRight(360/poligonoCostados);
        }
    }

    public static void costadoPlus(Turtle t, int costado) {

    }


}

public class Main {
    public static void main(String[] args) {
        int resultado = sumaNumeros(5, 4);
        System.out.println(resultado);

        Coche miCoche = new Coche();
        miCoche.aumentarPuerta();
        miCoche.aumentarPuerta();
        System.out.println(miCoche.puertas);
    }

    public static int sumaNumeros(int a, int b){
        return a + b;
    }

    public static class Coche{
        int puertas = 0;

        void aumentarPuerta(){
             puertas++;
        }
    }

}

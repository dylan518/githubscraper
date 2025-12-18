package Ejercicio10;

public class Ejercicio10 {
    private static char obtenerCaracter(){
        return switch((int)(Math.random()*6)){
            case 0->'*';
            case 1->'-';
            case 2->'=';
            case 3->'.';
            case 4->'|';
            case 5->'@';
            default->' ';
        };
    }
    public static void main(String[] args) {
        final int NUMERO_LINEAS = 10;
        for(int i=1;i<=NUMERO_LINEAS; i++){
            int columnas = (int)(Math.random()*40 + 1);
            char simbolo = obtenerCaracter();
            for(int j=1;j<=columnas;j++)
                System.out.printf("%s",simbolo);
            System.out.println();
        }
    }
    
}

package co.com.arreglos;

import java.util.Arrays;

public class EjemploArreglosForInverso {
    public static void main(String[] args) {

        //String[] productos = new String[7]; // Declaración de un arreglo de Strings con 7 elementos

        String[] productos = {
                "Kingston Pendrive 64GB",
                "Samsung Galaxy",
                "Disco Duro SSD Samsung Externo",
                "Asus Notebook", "Macbook Air",
                "Chromecast 4ta Generación",
                "Bicicleta Oxford"
        };
        
        int total = productos.length; // Obtiene la cantidad de elementos del arreglo

        /*productos[0] = "Kingston Pendrive 64GB";
        productos[1] = "Samsung Galaxy";
        productos[2] = "Disco Duro SSD Samsung Externo";
        productos[3] = "Asus Notebook";
        productos[4] = "Macbook Air";
        productos[5] = "Chromecast 4ta Generación";
        productos[6] = "Bicicleta Oxford";
        */

        Arrays.sort(productos); // Ordena el arreglo de Strings de forma ascendente (A-Z)

        for (int i = 0; i < total; i++) { // Recorre el arreglo de Strings
            System.out.println("Para indice " + i + " : " + productos[i]); // Imprime el valor del elemento en la posición i
        }

        System.out.println(" ===== Forma inversa 1 ===== ");
        // vamos a recorrer el arreglo de forma inversa
        for (int i = total - 1; i >= 0; i--) { // Recorre el arreglo de Strings
            System.out.println("Para indice " + i + " : " + productos[i]); // Imprime el valor del elemento en la posición i
        }

        System.out.println(" ===== forma inversa 2 ===== ");
        for (int i = 0; i < total; i++) {
            System.out.println("Para indice " + (total - 1 - i) + " : " + productos[total - 1 - i]);
        }

    }
}

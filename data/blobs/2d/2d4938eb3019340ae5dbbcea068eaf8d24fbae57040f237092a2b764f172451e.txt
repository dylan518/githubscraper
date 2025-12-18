package ficherostextoapuntes.E1004;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class LeerNumerosReales {
    public static void main(String[] args) {
        String linea = "";
        try {
            FileReader ficheroEntrada = new FileReader("UD07/1. APUNTES/ficherostextoapuntes/E1004/NumerosReales");
            BufferedReader bufferEntrada = new BufferedReader(ficheroEntrada);
            linea = bufferEntrada.readLine();

            String[] numeros = linea.split(" ");

            double suma = 0;
            for (String num : numeros) {
                suma += Double.parseDouble(num);
            }

            double media = suma / numeros.length;
            System.out.println("La suma es: " + suma);
            System.out.println("La media es: " + media);

            ficheroEntrada.close();
        } catch (FileNotFoundException ex) {
            System.out.println("No se encuentra el fichero");
        } catch (IOException ex) {
            System.out.println("Error.");
        }
    }
}

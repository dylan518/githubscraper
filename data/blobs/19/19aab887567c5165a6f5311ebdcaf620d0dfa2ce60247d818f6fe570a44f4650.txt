import java.util.Scanner;

/**
 * 
 *  158. Ejercicio 8: Pedir al usuario 2 cadenas de caracteres de números, uno entero y
    el otro real, convertirlos a sus respectivos valores y por último sumarlos. Realice un
    programa que lea una cadena de caracteres de la entrada estándar y muestre en la
    salida estándar cuántas ocurrencias de cada vocal existen en la cadena.
*/
public class Ejercicio158 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingresa dos cadenas de caracteres de numero (Entero, Real)");
        System.out.print("Entero: "); String enteroString = entrada.next();
        System.out.print("Real: "); String realString = entrada.next();

        int numeroEntero = Integer.parseInt(enteroString);
        double numeroReal = Double.parseDouble(realString);
        


        System.out.println("Ingresa una cadena para verificar las ocurrencias de las vocales");
        entrada.next();
        String cadenaEstandar = entrada.nextLine();
        entrada.close();
        int ocurrenciasDeA=0;
        int ocurrenciasDeE=0;
        int ocurrenciasDeI=0;
        int ocurrenciasDeO=0;
        int ocurrenciasDeU=0;

        for (int i = 0; i < cadenaEstandar.length(); i++) {
            if (cadenaEstandar.toLowerCase().charAt(i)=='a') {
                ocurrenciasDeA++;
            }

            if (cadenaEstandar.toLowerCase().charAt(i)=='e') {
                ocurrenciasDeE++;
            }

            if (cadenaEstandar.toLowerCase().charAt(i)=='i') {
                ocurrenciasDeI++;
            }

            if (cadenaEstandar.toLowerCase().charAt(i)=='o') {
                ocurrenciasDeO++;
            }

            if (cadenaEstandar.toLowerCase().charAt(i)=='u') {
                ocurrenciasDeU++;
            }
        }

        System.out.println("\nValores sumados: "+ (numeroEntero+numeroReal));

        System.out.println("\nCadena ingresada: "+cadenaEstandar);
        System.out.println("Ocurrencias de a: "+ocurrenciasDeA);
        System.out.println("Ocurrencias de e: "+ocurrenciasDeE);
        System.out.println("Ocurrencias de i: "+ocurrenciasDeI);
        System.out.println("Ocurrencias de o: "+ocurrenciasDeO);
        System.out.println("Ocurrencias de u: "+ocurrenciasDeU);

    }
}

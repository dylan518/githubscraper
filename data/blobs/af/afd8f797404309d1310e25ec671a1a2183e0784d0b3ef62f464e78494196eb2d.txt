package Persona.Login;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Crear un sistema de autenticación
        AuthenticationSystem authenticationSystem = new AuthenticationSystem();

        // Crear un objeto Scanner para la entrada del usuario
        Scanner scanner = new Scanner(System.in);

        int intentosRestantes = 3; // Número máximo de intentos

        while (intentosRestantes > 0) {
            // Pedir al usuario que ingrese el nombre de usuario y la contraseña
            System.out.print("Nombre de usuario: ");
            String nombreUsuario = scanner.nextLine();

            System.out.print("Contraseña: ");
            String contrasena = scanner.nextLine();

            if (authenticationSystem.autenticar(nombreUsuario, contrasena)) {
                System.out.println("Autenticación exitosa para el usuario: " + nombreUsuario);
                // Puedes agregar aquí la lógica específica para el tipo de trabajador
                break; // Salir del bucle si la autenticación es exitosa
            } else {
                System.out.println("Error de autenticación. Usuario o contraseña incorrectos.");
                intentosRestantes--;

                if (intentosRestantes > 0) {
                    System.out.println("Intentos restantes: " + intentosRestantes);
                } else {
                    System.out.println("Número máximo de intentos alcanzado. Programa finalizado.");
                }
            }
        }

        // Cerrar el Scanner
        scanner.close();
    }
}

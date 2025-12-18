package arrayobjetos;

import java.util.Scanner;
//Clase GestionEmpleados
public class GestionEmpleados {
    public static void main(String[] args) {
        // Verifica si se pasaron nombres como argumentos
        if (args.length  ==0) {
            System.out.println("Error, debes pasar al menos un nombre como argumento.");
        } else {
            // Imprime "Hola" + los nombres pasados como parámetros
            System.out.print("Hola ");
            for (String nombre : args) {
                System.out.print(nombre + " ");
            }
            System.out.println();

            // Inicia el programa de gestión de empleados
            gestionEmpleados();
        }
    }

    static void gestionEmpleados() {
        //Creamos el scanner
        Scanner scanner = new Scanner(System.in);

        // Declara un array de 5 objetos Empleado inicializado a null
        Empleado[] empleados = new Empleado[5];

        //Atributo opcion 
        int opcion;
        do {
            // Muestra el menú
            System.out.println("1. ALTA");
            System.out.println("2. CONSULTA");
            System.out.println("3. SALIR");
            System.out.print("Selecciona una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    // Opción ALTA: Inserta empleados en el array
                    altaEmpleado(empleados);
                    break;
                case 2:
                    // Opción CONSULTA: Muestra los datos de cada empleado
                    consultaEmpleados(empleados);
                    break;
                case 3:
                    // Opción SALIR: Finaliza el programa
                    System.out.println("Saliendo del programa. ¡Hasta luego!");
                    break;
                default:
                    System.out.println("Opción no válida. Inténtalo de nuevo.");
            }
        } while (opcion != 3);

        scanner.close(); //Cerramos el scanner
    }

    static void altaEmpleado(Empleado[] empleados) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < empleados.length; i++) {
            // Verifica si la posición está vacía (null)
            //Pedir los datos del empleado
            if (empleados[i] == null) {
                System.out.println("Introduce los datos del empleado:");
                System.out.print("DNI: ");
                String dni = scanner.next();
                System.out.print("Nombre: ");
                String nombre = scanner.next();
                System.out.print("Apellido: ");
                String apellido = scanner.next();
                System.out.print("Sueldo: ");
                double sueldo = scanner.nextDouble();

                // Crea un nuevo objeto Empleado y lo inserta en el array
                empleados[i] = new Empleado(dni, nombre, apellido, sueldo);

                System.out.println("Empleado dado de alta correctamente.");
                return;
            }
        }

        // Si el array está lleno, muestra un mensaje de error
        System.out.println("Error. No hay espacio para más empleados.");
    }

    static void consultaEmpleados(Empleado[] empleados) {
        // Recorre el array de empleados con un bucle foreach
        //Mostrar los datos del empleado
        System.out.println("Datos de los empleados:");
        for (Empleado empleado : empleados) {
            if (empleado != null) {
                System.out.println("DNI: " + empleado.dni);
                System.out.println("Nombre: " + empleado.nombre);
                System.out.println("Apellido: " + empleado.apellido);
                System.out.println("Sueldo: " + empleado.sueldo);
                System.out.println("--------------------------");
            }
        }
    }
}

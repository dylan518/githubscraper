package Parcial2;

import java.util.Scanner;

/**
 *
 * @author Wilmer Felipe Castellanos Salazar
 *  h. Hacer un menú para la gestión del Garaje, con estas opciones;
1.- Alquilar un espacio
2.- Retirar vehículo
3.- Consulta de ingresos mensuales
4.- Consulta proporción autos / motos
5.- Listado de matrículas y cuota mensual y tipo vehículo
    i. Se debe siempre controlar que:
• no se puedan alquilar más plazas de las existentes.
• no haya más del 80% de plazas ocupadas por motos.
• no se puede alquilar un vehículo si no tiene matricula.
 */
public class MenuGaraje {

    private static final int NUMERO_ESPACIOS = 10; // Constante para el número de espacios
    private static final Vehiculo[] espacios = new Vehiculo[NUMERO_ESPACIOS]; // Arreglo de espacios para vehículos

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n\n**Menú de gestión del Garaje**");
            System.out.println("1. Alquilar un espacio");
            System.out.println("2. Retirar vehículo");
            System.out.println("3. Consulta de ingresos mensuales");
            System.out.println("4. Consulta proporción autos / motos");
            System.out.println("5. Listado de matrículas y cuota mensual y tipo vehículo");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");

            opcion = scanner.nextInt();
            scanner.nextLine();

            switch (opcion) {
                case 1:
                    alquilarEspacio(scanner);
                    break;
                case 2:
                    retirarVehiculo(scanner);
                    break;
                case 3:
                    consultarIngresosMensuales();
                    break;
                case 4:
                    consultarProporcionAutosMotos();
                    break;
                case 5:
                    listarMatriculasCuotaTipoVehiculo();
                    break;
                case 0:
                    System.out.println("Saliendo del menú...");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        } while (opcion != 0);

        scanner.close();
    }

    // 1
    private static void alquilarEspacio(Scanner scanner) {
        System.out.print("Ingrese la matrícula del vehículo: ");
        String placa = scanner.nextLine();

        System.out.print("Ingrese la marca del vehículo: ");
        String marca = scanner.nextLine();

        System.out.print("Ingrese el precio del vehículo: ");
        double precio = scanner.nextDouble();

        System.out.print("Ingrese el cilindraje del vehículo: ");
        int cilindraje = scanner.nextInt();

        scanner.nextLine();

        System.out.print("¿Tiene sidecar (moto) o radio y navegador (auto)? (s/n): ");
        String tieneExtras = scanner.nextLine();

        Vehiculo vehiculo;
        if (tieneExtras.equalsIgnoreCase("s")) {
            System.out.print("¿Tiene sidecar? (s/n): ");
            String tieneSidecar = scanner.nextLine();

            if (tieneSidecar.equalsIgnoreCase("s")) {
                vehiculo = new Moto(true, placa, marca, precio, cilindraje);
            } else {
                vehiculo = new Auto(true, true, placa, marca, precio, cilindraje);
            }
        } else {
            vehiculo = new Vehiculo(placa, marca, precio, cilindraje);
        }

        if (hayEspacioDisponible()) {
            if (vehiculo.getPlaca() != null && !vehiculo.getPlaca().isEmpty()) {
                if (esValidoAlquilarMoto(vehiculo) || esValidoAlquilarAuto(vehiculo)) {
                    ingresarVehiculo(vehiculo);
                    System.out.println("Vehículo alquilado correctamente.");
                } else {
                    System.out.println("No se puede alquilar el vehículo. Revise las condiciones.");
                }
            } else {
                System.out.println("El vehículo no tiene matrícula.");
            }
        } else {
            System.out.println("Lo sentimos, no hay espacios disponibles en este momento.");
        }
    }

    //2
    private static void retirarVehiculo(Scanner scanner) {
        System.out.print("Ingrese la matrícula del vehículo: ");
        String placa = scanner.nextLine();

        Vehiculo vehiculo = buscarVehiculo(placa);
        if (vehiculo != null) {
            retirarVehiculo(vehiculo);
            System.out.println("Vehículo retirado correctamente.");
        } else {
            System.out.println("No se encontró el vehículo con esa matrícula.");
        }
    }

    //3
    private static void consultarIngresosMensuales() {
        double ingresosTotales = 0.0;
        for (Vehiculo vehiculo : espacios) {
            if (vehiculo != null) {
                ingresosTotales += vehiculo.getCuotaMesGaraje();
            }
        }
        System.out.println("Ingresos mensuales: " + ingresosTotales);
    }

    //4
    private static void consultarProporcionAutosMotos() {
        int ocupacionMotos = 0;
        int ocupacionAutos = 0;
        for (Vehiculo vehiculo : espacios) {
            if (vehiculo != null) {
                if (vehiculo instanceof Moto) {
                    ocupacionMotos++;
                } else if (vehiculo instanceof Auto) {
                    ocupacionAutos++;
                }
            }
        }

        int totalVehiculos = ocupacionMotos + ocupacionAutos;
        if (totalVehiculos > 0) {
            double proporcionMotos = (ocupacionMotos * 100.0) / totalVehiculos;
            double proporcionAutos = (ocupacionAutos * 100.0) / totalVehiculos;
            System.out.println("Proporción motos: " + proporcionMotos + "%");
            System.out.println("Proporción autos: " + proporcionAutos + "%");
        } else {
            System.out.println("No hay vehículos en el garaje.");
        }
    }

    //5
    private static void listarMatriculasCuotaTipoVehiculo() {
    System.out.println("Listado de matrículas, cuota mensual y tipo de vehículo:");
    System.out.printf("%-20s %-15s %-10s\n", "Matrícula", "Cuota", "Tipo");

    for (Vehiculo vehiculo : espacios) {
        if (vehiculo != null) {
            String tipoVehiculo;
            if (vehiculo instanceof Moto) {
                tipoVehiculo = "Moto";
            } else if (vehiculo instanceof Auto) {
                tipoVehiculo = "Auto";
            } else {
                tipoVehiculo = "Otro";
            }

            System.out.printf("%-20s %-15.2f %-10s\n", vehiculo.getPlaca(), vehiculo.getCuotaMesGaraje(), tipoVehiculo);
        }
    }
}

    // Métodos auxiliares
    private static boolean hayEspacioDisponible() {
        for (Vehiculo vehiculo : espacios) {
            if (vehiculo == null) {
                return true;
            }
        }
        return false;
    }

    private static boolean esValidoAlquilarMoto(Vehiculo vehiculo) {
        int ocupacionMotos = 0;
        for (Vehiculo vehiculoGaraje : espacios) {
            if (vehiculoGaraje != null && vehiculoGaraje instanceof Moto) {
                ocupacionMotos++;
            }
        }

        if (ocupacionMotos < (NUMERO_ESPACIOS * 0.8)) {
            return true;
        } else {
            System.out.println("No se pueden alquilar más motos. Se ha superado el límite del 80%.");
            return false;
        }
    }

    private static boolean esValidoAlquilarAuto(Vehiculo vehiculo) {
        return true;
    }

    private static void ingresarVehiculo(Vehiculo vehiculo) {
        for (int i = 0; i < NUMERO_ESPACIOS; i++) {
            if (espacios[i] == null) {
                espacios[i] = vehiculo;
                break;
            }
        }
    }

    private static void retirarVehiculo(Vehiculo vehiculo) {
        for (int i = 0; i < NUMERO_ESPACIOS; i++) {
            if (espacios[i] != null && espacios[i].equals(vehiculo)) {
                espacios[i] = null;
                break;
            }
        }
    }

    private static Vehiculo buscarVehiculo(String placa) {
        for (Vehiculo vehiculo : espacios) {
            if (vehiculo != null && vehiculo.getPlaca().equals(placa)) {
                return vehiculo;
            }
        }
        return null;
    }
}

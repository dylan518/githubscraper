import java.util.Scanner;

public class GestionClientes {

    public static void gestionarClientes(VeterinariaManager manager, Scanner scanner) {
        int opcion;
        do {
            System.out.println("\n--- Gestión de Clientes ---");
            System.out.println("1. Agregar Cliente");
            System.out.println("2. Buscar Cliente");
            System.out.println("3. Actualizar Cliente");
            System.out.println("4. Eliminar Cliente");
            System.out.println("5. Volver");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese nombre del cliente: ");
                    String nombre = scanner.nextLine();
                    System.out.print("Ingrese email del cliente: ");
                    String email = scanner.nextLine();
                    manager.agregar(new Cliente(nombre, email));
                    System.out.println("Cliente agregado con éxito.");
                    break;
                case 2:
                    System.out.print("Ingrese el nombre del cliente a buscar: ");
                    nombre = scanner.nextLine();
                    Cliente cliente = manager.buscar(nombre);
                    if (cliente != null) {
                        System.out.println(
                                "Cliente encontrado: " + cliente.getNombre() + " (" + cliente.getEmail() + ")");
                    } else {
                        System.out.println("Cliente no encontrado.");
                    }
                    break;
                case 3:
                    System.out.print("Ingrese el nombre del cliente a actualizar: ");
                    nombre = scanner.nextLine();
                    Cliente clienteActualizar = manager.buscar(nombre);
                    if (clienteActualizar != null) {
                        System.out.print("Ingrese el nuevo email: ");
                        String nuevoEmail = scanner.nextLine();
                        clienteActualizar.setEmail(nuevoEmail);
                        System.out.println("Cliente actualizado con éxito.");
                    } else {
                        System.out.println("Cliente no encontrado.");
                    }
                    break;
                case 4:
                    System.out.print("Ingrese el nombre del cliente a eliminar: ");
                    nombre = scanner.nextLine();
                    manager.eliminar(nombre);
                    System.out.println("Cliente eliminado si existía.");
                    break;
                case 5:
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        } while (opcion != 5);
    }
}

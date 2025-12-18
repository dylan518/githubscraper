package Servicios;

import Entidades.Producto;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

public class ServicioProducto {

    Scanner leer = new Scanner(System.in);

    public void menu(HashMap<String, Producto> inventario) {
        Integer i;

        do {
            System.out.println("Menu de inventario");
            System.out.println("1. Introducir nuevo producto");
            System.out.println("2. Modificar precio de un producto");
            System.out.println("3. Eliminar un producto");
            System.out.println("4. Buscar producto");
            System.out.println("5. Mostar lista de productos");
            i = leer.nextInt();
            switch (i) {
                case 1:
                    Llenarmapa(inventario);

                    break;
                case 2:
                    modificarprecio(inventario);

                    break;
                case 3:
                    eliminarproducto(inventario);

                    break;
                case 4:
                    buscarproducto(inventario);

                    break;
                case 5:
                    mostrarinventario(inventario);
                    break;

            }
        } while (i != 6);

    }

    public Producto crearProducto() {
        Producto p = new Producto();
        System.out.println("Ingrese el Nombre del Producto");
        p.setNombreProducto(leer.next());
        System.out.println("Ingrese el Precio del Producto");
        p.setPrecio(leer.nextInt());
        return p;
    }

    public void Llenarmapa(HashMap<String, Producto> inventario) {
        String r;
        Producto p;
        do {
            p = crearProducto();
            inventario.put(p.getNombreProducto(), p);
            System.out.println("Desea agregar otro Producto S/N");
            r = leer.next();
        } while (r.equalsIgnoreCase("S"));

    }

    public void modificarprecio(HashMap<String, Producto> inventario) {
        ArrayList<Producto> inventario1 = new ArrayList(inventario.values());
        System.out.println("Ingrese nombre del producto a modificar precio");
        String buscar = leer.next();
        Producto buscar1 = new Producto();

        for (Producto producto : inventario1) {
            if (producto.getNombreProducto().equalsIgnoreCase(buscar)) {
                System.out.println("Ingrese nuevo precio del producto");
                producto.setPrecio(leer.nextInt());
                buscar1 = producto;
            }
        }

        for (Map.Entry<String, Producto> entry : inventario.entrySet()) {
            String key = entry.getKey();
            Producto value = entry.getValue();
            if (value.getNombreProducto().equalsIgnoreCase(buscar)) {
                entry.setValue(buscar1);
            }
        }

    }

    public void eliminarproducto(HashMap<String, Producto> inventario) {
        System.out.println("Ingrese producto a eliminar");
        String producto = leer.next();
        Boolean noexiste = false;

        for (Iterator<String> it = inventario.keySet().iterator(); it.hasNext();) {
            String key = it.next();
            if (key.equalsIgnoreCase(producto)) {
                noexiste = true;
                it.remove();
            }
        }

        if (noexiste) {
            System.out.println("El producto " + producto + " fue eliminado.");
        } else {
            System.out.println(" El producto " + producto + " no existe.");
        }
    }

    public void mostrarinventario(HashMap<String, Producto> inventario) {
        ArrayList<Producto> imprimir = new ArrayList(inventario.values());

        imprimir.forEach((producto) -> {
            System.out.println(producto.toString());
        });
    }

    public void buscarproducto(HashMap<String, Producto> inventario) {
        System.out.println("Ingrese producto a mostrar");
        String productobuscar = leer.next();
        Boolean noexiste = false;
        Producto buscado = new Producto();
        for (Map.Entry<String, Producto> entry : inventario.entrySet()) {
            String key = entry.getKey();
            Producto value = entry.getValue();
            if (key.equalsIgnoreCase(productobuscar)) {
                System.out.println(value.toString());
                noexiste = true;
            }
        }
        if (noexiste) {
            System.out.println("El producto " + productobuscar + " fue encontrado");
        } else {
            System.out.println(" El producto " + productobuscar + " no existe.");
        }

    }
}

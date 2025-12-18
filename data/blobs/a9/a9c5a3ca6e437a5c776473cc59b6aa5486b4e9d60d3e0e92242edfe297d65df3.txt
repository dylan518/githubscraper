package com.aluraoracle.hotelalura.prueba;

import com.aluraoracle.hotelalura.DAO.TipoHabitacionDao;
import com.aluraoracle.hotelalura.logica.TipoHabitacion;
import java.util.List;

public class PruebaTipoHabitacion {
 
    public static void main(String[] args) {
       
        TipoHabitacionDao tipoHabitacionDao = new TipoHabitacionDao();
        // Registrar una nueva persona
        registrarTipoHabitacion(tipoHabitacionDao);

        // Cerrar el EntityManagerFactory
        tipoHabitacionDao.cerrarEntityManagerFactory();
    }
    
   private static void registrarTipoHabitacion(TipoHabitacionDao tipoHabitacionDao){
    
    TipoHabitacion tipoHabitacion = new TipoHabitacion("SIMPLE",20,true);
    TipoHabitacion resultado = tipoHabitacionDao.registrarTipoHabitacion(tipoHabitacion);
    
    if(resultado != null){
        System.out.println("Tipo de habitacion registrada con exito: "+ resultado.getNombre());
    }else{
        System.out.println("La habitación ya existe o no se pudo registrar.");
        }    
    }
   
   private static void actualizarTipoHabitacion(TipoHabitacionDao tipoHabitacionDao){
   
       Long idTipoHabitacion = 1L; // ID de la habitacion que deseas actualizar.
       String nuevoNombre = "matrimonial";   //nuevo nombre
       double nuevoPrecio = 100;   //nuevo precio
       
       // Llama al método para actualizar el nombre del tipo de habitación.
       TipoHabitacion tipoHabitacionActualizada = tipoHabitacionDao.actualizarTipoHabitacion(idTipoHabitacion, nuevoNombre, nuevoPrecio);
       
       if(tipoHabitacionActualizada != null){
           System.out.println("Tipo de habitacion actualizada con exito");
       }else{
           System.out.println("No se puedo actualizar tipo de habitacion");
       }
       
        tipoHabitacionDao.cerrarEntityManagerFactory(); // Cierra el EntityManagerFactory cuando ya no lo necesitas.
   }
   
   private static void buscarTipoHabitacionPorNombre(TipoHabitacionDao tipoHabitacionDao){
        
        String nombre = "nuevaHabitacion";
        TipoHabitacion tipoHabitacion = tipoHabitacionDao.buscarTipoHabitacionPorNombre(nombre);

        if (tipoHabitacion != null) {
            System.out.println("Tipo de habitación encontrado: " + tipoHabitacion.getNombre());
        } else {
            System.out.println("Tipo de habitacion no encontrado.");
        }
   }
   
   
   private static void buscarTipoHabitacionPorId(TipoHabitacionDao tipoHabitacionDao){
   
        Long idTipoHabitacion = 1L;
        TipoHabitacion tipoHabitacionEncontrado = tipoHabitacionDao.buscarTipoHabitacionPorId(idTipoHabitacion);

        if (tipoHabitacionEncontrado != null) {
            System.out.println("Tipo de habitación encontrado: " + tipoHabitacionEncontrado.getId());
        } else {
            System.out.println("Tipo de habitacion no encontrado.");
        }
   }
  

   private static void eliminarTipoHabitacion(TipoHabitacionDao tipoHabitacionDao){
   
       Long idTipoHabitacion = 1L; // Obtener el ID del tipo de habitacion a eliminar (reemplaza con un ID válido)
       
       boolean eliminacionExitosa = tipoHabitacionDao.eliminarTipoHabitacion(idTipoHabitacion);

        if (eliminacionExitosa) {
            System.out.println("Tipo de habitación eliminada lógicamente con éxito. ID: " + idTipoHabitacion);
        } else {
            System.out.println("No se pudo eliminar el tipo de habitación o no existe.");
        }
   }

   
    private static void listarTodasLasTipoHabitacion(TipoHabitacionDao tipoHabitacionDao) {
        // Listar todas los tipos de habitaciones activas
        List<TipoHabitacion> tipoHabitaciones= tipoHabitacionDao.listarTodasLasTipoHabitacion();

        if (!tipoHabitaciones.isEmpty()) {
            System.out.println("Listado de tipos de habitaciones activas:");
            for (TipoHabitacion tipoHabitacion : tipoHabitaciones) {
                System.out.println(tipoHabitacion.getId() + ": " + tipoHabitacion.getNombre() + " " + tipoHabitacion.getPrecio()) ;
            }
        } else {
            System.out.println("No se encontraron tipos de habitaciones activas.");
        }
    }
   
}

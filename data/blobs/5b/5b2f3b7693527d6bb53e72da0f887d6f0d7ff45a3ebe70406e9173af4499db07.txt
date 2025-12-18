package org.example.controlador;

import java.util.List;

import org.example.modelo.Estudio;
import org.example.repositorio.RepositorioEstudio;
import org.example.servicio.ServicioEstudio;

import com.mongodb.client.MongoDatabase;

public class ControladorEstudio {
    private ServicioEstudio servicioEstudio;

    public ControladorEstudio(MongoDatabase database){
        RepositorioEstudio repositorioEstudio = new RepositorioEstudio(database);
        this.servicioEstudio = new ServicioEstudio(repositorioEstudio);
    }

    public void crearEstudio(String nombre, String ubicacion){
        servicioEstudio.crearEstudio(nombre, ubicacion);
    }

    public Estudio obtenerEstudioPorId(String id){
        return servicioEstudio.obtenerEstudioPorId(id);
    }

    public List<Estudio> obtenerTodo(){
      return servicioEstudio.obtenerTodosLosEstudios();
    }

    public void actualizarEstudio(String id, String nombre, String ubicacion){
        servicioEstudio.actualizarEstudio(id, nombre, ubicacion);
    }

    public void eliminarEstudio(String id){
        servicioEstudio.eliminarEstudio(id);
    }
}

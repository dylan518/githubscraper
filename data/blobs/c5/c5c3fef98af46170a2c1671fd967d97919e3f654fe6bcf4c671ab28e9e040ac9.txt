package com.example.CompucaliTVPro.web.controlador;


import com.example.CompucaliTVPro.dominio.servicioImpl.ContenidoServicioImpl;
import com.example.CompucaliTVPro.persistencia.DTO.ContenidoDTO;
import org.springframework.data.repository.query.Param;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/contenido")
public class ContenidoControlador {

    private final ContenidoServicioImpl contenidoServicio;

    public ContenidoControlador(ContenidoServicioImpl contenidoServicio){
        this.contenidoServicio = contenidoServicio;
    }

    @GetMapping("/miContenido/{usuarioId}")
    ResponseEntity<List<Object>> obtenerTodosMisContenidos(@PathVariable int usuarioId){
        return ResponseEntity.ok(contenidoServicio.obtenerTodosMisContenidos(usuarioId));
    }


}

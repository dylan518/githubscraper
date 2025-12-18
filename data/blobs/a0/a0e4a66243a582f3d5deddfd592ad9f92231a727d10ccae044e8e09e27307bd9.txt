package com.practica.eventos.service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.practica.eventos.dto.OficioDto;
import com.practica.eventos.model.Oficio;
import com.practica.eventos.model.Sede;
import com.practica.eventos.model.TipoDeEventos;
import com.practica.eventos.repository.OficioRepository;
import com.practica.eventos.repository.SedeRepository;
import com.practica.eventos.repository.TipoDeEventosRepository;

@Service
public class OficioService {
    @Autowired
    private OficioRepository oficioRepository;

    @Autowired
    private TipoDeEventosRepository tipoDeEventosRepository;

    @Autowired
    private SedeRepository sedeRepository;

    public List<Oficio> getAllOficios() {
        return oficioRepository.findAll();
    }

    public Optional<Oficio> getOficioById(String id) {
        return oficioRepository.findById(id);
    }

    public Oficio createOficio(OficioDto oficioDTO) {
        if (oficioDTO == null) {
            throw new RuntimeException("El objeto oficioDTO no debe ser nulo");
        }
    
        if (oficioDTO.getTipoDeEventoId() == null) {
            throw new RuntimeException("El ID del tipo de evento no debe ser nulo");
        }
    
        if (oficioDTO.getSedeId() == null) {
            throw new RuntimeException("El ID de la sede no debe ser nulo");
        }
        
        // Buscar TipoDeEventos por ID
        TipoDeEventos tipoDeEvento = tipoDeEventosRepository.findById(oficioDTO.getTipoDeEventoId()).orElseThrow(() -> new RuntimeException("Evento no encontrado"));

        // Buscar Sede por ID
        Sede sede = sedeRepository.findById(oficioDTO.getSedeId()).orElseThrow(() -> new RuntimeException("Evento no encontrado"));

        // Convertir LocalDateTime desde el formato String
        LocalDateTime fechaOficio = null;
        if (oficioDTO.getFechaOficio() != null) {
            fechaOficio = oficioDTO.getFechaOficio();  // Asegúrate de que el formato sea correcto
        }

        // Crear un nuevo Oficio
        Oficio oficio = new Oficio();
        oficio.setNoControl(oficioDTO.getNoControl());
        oficio.setNoOficio(oficioDTO.getNoOficio());
        oficio.setFechaOficio(fechaOficio);
        oficio.setTipoDeEvento(tipoDeEvento);  // Relacionar con TipoDeEventos
        oficio.setSede(sede);                  // Relacionar con Sede

        // Guardar el Oficio
        return oficioRepository.save(oficio);
    }

    public Oficio updateOficio(String id, OficioDto oficioDTO) {
        if (oficioDTO == null) {
            throw new RuntimeException("El objeto oficioDTO no debe ser nulo");
        }
    
        if (oficioDTO.getTipoDeEventoId() == null) {
            throw new RuntimeException("El ID del tipo de evento no debe ser nulo");
        }
    
        if (oficioDTO.getSedeId() == null) {
            throw new RuntimeException("El ID de la sede no debe ser nulo");
        }
    
        // Buscar el Oficio existente por ID
        Oficio oficioExistente = oficioRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Oficio no encontrado"));
    
        // Buscar TipoDeEventos por ID
        TipoDeEventos tipoDeEvento = tipoDeEventosRepository.findById(oficioDTO.getTipoDeEventoId())
            .orElseThrow(() -> new RuntimeException("Evento no encontrado"));
    
        // Buscar Sede por ID
        Sede sede = sedeRepository.findById(oficioDTO.getSedeId())
            .orElseThrow(() -> new RuntimeException("Sede no encontrada"));
    
        // Convertir LocalDateTime desde el formato String (si se proporciona)
        LocalDateTime fechaOficio = null;
        if (oficioDTO.getFechaOficio() != null) {
            fechaOficio = oficioDTO.getFechaOficio();  // Asegúrate de que el formato sea correcto
        }
    
        // Actualizar los campos del Oficio
        oficioExistente.setNoControl(oficioDTO.getNoControl());
        oficioExistente.setNoOficio(oficioDTO.getNoOficio());
        oficioExistente.setFechaOficio(fechaOficio);
        oficioExistente.setTipoDeEvento(tipoDeEvento);  // Relacionar con TipoDeEventos
        oficioExistente.setSede(sede);                  // Relacionar con Sede
    
        // Guardar el Oficio actualizado
        return oficioRepository.save(oficioExistente);
    }

    public void deleteOficio(String id) {
        oficioRepository.deleteById(id);
    }
}

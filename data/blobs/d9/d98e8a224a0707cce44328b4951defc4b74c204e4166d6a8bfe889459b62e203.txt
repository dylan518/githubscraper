package com.hiramwoki.ForoHub_HiramAcevedo.controller;

import com.hiramwoki.ForoHub_HiramAcevedo.dto.DatosActualizacionTopico;
import com.hiramwoki.ForoHub_HiramAcevedo.dto.DatosDetalleTopico;
import com.hiramwoki.ForoHub_HiramAcevedo.dto.DatosListadoTopico;
import com.hiramwoki.ForoHub_HiramAcevedo.dto.DatosRegistroTopico;
import com.hiramwoki.ForoHub_HiramAcevedo.exception.TopicoNotFoundException;
import com.hiramwoki.ForoHub_HiramAcevedo.model.Topico;
import com.hiramwoki.ForoHub_HiramAcevedo.repository.TopicoRepository;
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.util.UriComponentsBuilder;

import java.util.List;

@RestController
@RequestMapping("/topicos")
public class TopicoController {

    @Autowired
    private TopicoRepository repository;

    @PostMapping
    public ResponseEntity<Topico> registrarTopico(@RequestBody @Valid DatosRegistroTopico datos, UriComponentsBuilder uriBuilder) {
        Topico topico = new Topico(datos.titulo(), datos.mensaje(), datos.autor(), datos.curso());
        repository.save(topico);

        var uri = uriBuilder.path("/topicos/{id}").buildAndExpand(topico.getId()).toUri();
        return ResponseEntity.created(uri).body(topico);
    }

    @GetMapping
    public ResponseEntity<List<DatosListadoTopico>> listarTopicos() {
        List<DatosListadoTopico> topicos = repository.findAll().stream()
                .map(DatosListadoTopico::new)
                .toList();
        return ResponseEntity.ok(topicos);
    }

    @GetMapping("/{id}")
    public ResponseEntity<DatosDetalleTopico> detallarTopico(@PathVariable Long id) {
        Topico topico = repository.findById(id)
                .orElseThrow(() -> new TopicoNotFoundException("Tópico no encontrado con ID: " + id));
        return ResponseEntity.ok(new DatosDetalleTopico(topico));
    }

    @PutMapping
    @Transactional
    public ResponseEntity<DatosDetalleTopico> actualizarTopico(@RequestBody @Valid DatosActualizacionTopico datos) {
        Topico topico = repository.findById(datos.id())
                .orElseThrow(() -> new TopicoNotFoundException("Tópico no encontrado con ID: " + datos.id()));

        topico.actualizarInformacion(datos);

        return ResponseEntity.ok(new DatosDetalleTopico(topico));
    }

    @DeleteMapping("/{id}")
    @Transactional
    public ResponseEntity<?> eliminarTopico(@PathVariable Long id) {
        if (!repository.existsById(id)) {
            throw new TopicoNotFoundException("Tópico no encontrado con ID: " + id);
        }
        repository.deleteById(id);
        return ResponseEntity.noContent().build();
    }

}

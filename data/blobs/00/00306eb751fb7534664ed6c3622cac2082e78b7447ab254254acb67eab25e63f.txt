package com.example.project_crud.controllers;

import com.example.project_crud.repositories.VoluntarioResporitory;
import com.example.project_crud.entities.Voluntarios;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;


@RestController
@RequestMapping(value = "/voluntario")
public class VoluntariosController {
    @Autowired
    private VoluntarioResporitory voluntarioRepository;

    @GetMapping
    public List<Voluntarios> findAll(){
        return voluntarioRepository.findAll();
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<Voluntarios> findById(@PathVariable Long id){
        Optional<Voluntarios> voluntario = voluntarioRepository.findById(id);
        return voluntario.map(response -> ResponseEntity.ok().body(response)).orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Voluntarios insert(@RequestBody Voluntarios voluntarios){
        return voluntarioRepository.save(voluntarios);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Voluntarios> update(@PathVariable Long id, @RequestBody Voluntarios novosVoluntarios){
        Optional<Voluntarios> voluntarioOptional = voluntarioRepository.findById(id);

        if(voluntarioOptional.isPresent()){
            Voluntarios voluntario = voluntarioOptional.get();
            voluntario.setNome(novosVoluntarios.getNome());
            voluntario.setEmail(novosVoluntarios.getEmail());
            voluntario.setTelefone(novosVoluntarios.getTelefone());
            voluntario.setHabilidades(novosVoluntarios.getHabilidades());
            voluntario.setDisponibilidade(novosVoluntarios.getDisponibilidade());
            voluntario.setAtivo(novosVoluntarios.getAtivo());
            Voluntarios resultato = voluntarioRepository.save(voluntario);
            return ResponseEntity.ok(resultato);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Voluntarios> delete(@PathVariable Long id){
        Optional<Voluntarios> voluntarioOptional = voluntarioRepository.findById(id);
        
        if(voluntarioOptional.isPresent()){
            voluntarioRepository.deleteById(id);
            return ResponseEntity.ok().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}

package com.practica.busesback.Controller;


import com.practica.busesback.Service.AsientosService;
import com.practica.busesback.Service.ProgramacionService;
import com.practica.busesback.models.Asiento;
import com.practica.busesback.models.Programacion;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("api/programacion")
public class ProgramacionController {

    @Autowired
    private ProgramacionService programacionService;

    @PostMapping("/save")
    public ResponseEntity<Programacion> Save(@RequestBody Programacion programacion){
        programacionService.guardarProgramacion(programacion);
        return new ResponseEntity<>(programacion, HttpStatus.CREATED);
    }

    @PutMapping("/update")
    public ResponseEntity<Programacion> Update(@RequestBody Programacion programacion){
        programacionService.guardarProgramacion(programacion);
        return new ResponseEntity<>(programacion, HttpStatus.CREATED);
    }

    @PutMapping("/delete/{id}")
    public ResponseEntity<?> Delete(@PathVariable Long id){
        programacionService.eliminarProgramacion(id);
        return new ResponseEntity<>(null, HttpStatus.OK);
    }

    @GetMapping ("/listar")
    public ResponseEntity<List<Programacion>> List(){
        return new ResponseEntity<List<Programacion>>(programacionService.listaProgramacion(), HttpStatus.OK);
    }
}

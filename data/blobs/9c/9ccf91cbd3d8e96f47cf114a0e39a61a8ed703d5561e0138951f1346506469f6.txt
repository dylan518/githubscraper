package com.example.crudejercicio.controller;

import com.example.crudejercicio.entity.StudentEntity;
import com.example.crudejercicio.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/student")
public class StudentController {

    @Autowired //enlace con el servicio
    private StudentService studentService; //constante

    @GetMapping //obtiene los datos de los estudiantes
    public List<StudentEntity> getall() {
        return studentService.getstudents();
    }

    @GetMapping("/{id}") //filtrado de estudiates por id
    public Optional<StudentEntity> getByid(@PathVariable("id") Long id){
        return studentService.getstudent(id);

    }

    @PostMapping
    public void save(@RequestBody StudentEntity studentEntity){
        studentService.save(studentEntity);
    }

    @PutMapping
    public void Update(@RequestBody StudentEntity studentEntity) {
        studentService.update(studentEntity);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable("id") Long id){
        studentService.delete(id);
    }

}

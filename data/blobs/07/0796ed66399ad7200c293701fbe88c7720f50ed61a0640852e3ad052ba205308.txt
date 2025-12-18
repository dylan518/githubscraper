package com.harsh.assignment.controller;


import com.harsh.assignment.pojo.internal.Student;
import com.harsh.assignment.pojo.internal.Subject;
import com.harsh.assignment.service.StudentService;
import com.harsh.assignment.service.SubjectService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.Set;

@RestController
@RequestMapping("/student")
public class StudentController {

    @Autowired
    private StudentService service;

    @PostMapping
    @PreAuthorize("hasRole('STUDENT')")
    public ResponseEntity<String> createStudent(@RequestBody Student student){

        String s=service.create(student);

        return new ResponseEntity<>("Student created : " + s, HttpStatus.CREATED);
    }

    @GetMapping
    @PreAuthorize("hasRole('STUDENT')")
    public ResponseEntity<Set<Student>> getAllStudent(){

        Set<Student> students=service.getAll();

        return new ResponseEntity<>(students, HttpStatus.OK);
    }
}

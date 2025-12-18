package com.yago_microservices.department.controller;

import com.yago_microservices.department.entity.Department;
import com.yago_microservices.department.service.DepartmentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/departments")
public class DepartmentController {
    @Autowired
    DepartmentService departmentService;
    @GetMapping
    public List<Department> getAll(){
        return departmentService.getAll();
    }

    @GetMapping("{id}")
    public ResponseEntity<Department> getDepartmentById(@PathVariable("id") Long departmentId){
        Department department = departmentService.getDepartmentById(departmentId);
        return ResponseEntity.ok(department);
    }

    @PostMapping
    public Department save(@RequestBody Department department){
        return departmentService.save(department);
    }
}

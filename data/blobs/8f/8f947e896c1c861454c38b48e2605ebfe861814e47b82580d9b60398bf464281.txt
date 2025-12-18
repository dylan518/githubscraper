package com.spring1.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.spring1.demo.entity.Department;
import com.spring1.demo.service.DepartmentService;

/**
 * DepartmentController
 */
@RestController
public class DepartmentController {
    
    @Autowired
    private  DepartmentService departmentService;
    @PostMapping("/departments")
    public Department saveDepartment(@RequestBody Department department){
        return departmentService.saveDepartment(department);
    }
    @GetMapping("/departments")
    public java.util.List<Department> fetchDepartmentList(){
        return departmentService.fetchDepartmentList();
    }
    
    @GetMapping("/departments/{id}")
    public Department fetchDepartmentbyId(@PathVariable("id") Long departmentId){
        return departmentService.fetchDepartmentbyId(departmentId);
    }

    @DeleteMapping("/departments/{id}")
    public String deleteDepartmentbyId(@PathVariable("id") Long departmentId){
        departmentService.deleteDepartmentbyId(departmentId);
        return "deleted!";
    }

    @PutMapping("/departments/{id}")
    public Department updateDepartment(@PathVariable("id") Long departmentID , @RequestBody Department department){
        return departmentService.updateDepartment(departmentID,department);
    }
}
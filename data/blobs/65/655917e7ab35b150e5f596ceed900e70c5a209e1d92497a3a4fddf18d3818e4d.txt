package com.atuluttam.SpringBootJPAOnetoManyMappingUniDirectional.Service;

import com.atuluttam.SpringBootJPAOnetoManyMappingUniDirectional.Model.Department;
import com.atuluttam.SpringBootJPAOnetoManyMappingUniDirectional.Model.Student;
import com.atuluttam.SpringBootJPAOnetoManyMappingUniDirectional.Repository.DepartmentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Set;

@Service
public class DepartmentService {

    @Autowired
    private DepartmentRepository departmentRepository;

    // Method to add a new department
    public Department addDepartment(Department department) {
        return departmentRepository.save(department);
    }

    // Method to add students to a department
    public Department addStudentsToDepartment(Long departmentId, Set<Student> students) {
        Department department = departmentRepository.findById(departmentId)
                .orElseThrow(() -> new RuntimeException("Department not found"));

        department.getStudents().addAll(students);
        return departmentRepository.save(department);
    }

    // Method to get all students in a department
    public Set<Student> getAllStudentsByDepartmentId(Long departmentId) {
        Department department = departmentRepository.findById(departmentId)
                .orElseThrow(() -> new RuntimeException("Department not found"));

        return department.getStudents();
    }

    // Method to get all departments
    public List<Department> getAllDepartments() {
        return departmentRepository.findAll();
    }

    // Method to get a department by its ID
    public Department getDepartmentById(Long departmentId) {
        return departmentRepository.findById(departmentId)
                .orElseThrow(() -> new RuntimeException("Department not found"));
    }

    // Method to delete a department
    public void deleteDepartment(Long departmentId) {
        departmentRepository.deleteById(departmentId);
    }
}
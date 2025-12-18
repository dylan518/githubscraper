package com.immenser.interserv.controllers;

import com.immenser.interserv.models.Employee;
import com.immenser.interserv.services.EmployeeService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/employees")
@RequiredArgsConstructor
public class EmployeeController {

    private final EmployeeService employeeService;

    @GetMapping("/{id}")
    public ResponseEntity<Employee> findEmployee(@PathVariable Long id) {
        Employee employee = employeeService.findEmployee(id);
        return ResponseEntity.ok(employee);
    }

    @PostMapping
    public void addEmployee(@RequestBody Employee employee){
        employeeService.addEmployee(employee);
    }

    @GetMapping
    public List<Employee> findEmployeesByGroupAndPosition(@RequestParam("groupId") long groupId, @RequestParam("position") String position) {
        return employeeService.findEmployeesByGroupAndPosition(groupId, position);
    }

    @GetMapping("/free")
    public List<Employee> findFreeEmployeesByPeriodAndAgeAndPosition(@RequestParam("periodId") long periodId,
                                                                     @RequestParam("ageId") long ageId,
                                                                     @RequestParam("position") String position) {
        return employeeService.findFreeEmployeesByPeriodAndAgeAndPosition(periodId, ageId, position);
    }
}
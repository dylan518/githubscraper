package com.ritesh.EmployeeMS.controller;

import com.ritesh.EmployeeMS.model.Employee;
import com.ritesh.EmployeeMS.service.EmployeeService;
import com.ritesh.EmployeeMS.service.ReportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class EmployeeController {

    @Autowired
    EmployeeService employeeService;

    @Autowired
    ReportService reportService;

    @GetMapping("your/details")
    public Employee getYourDetails(@RequestParam Long empId){
        return employeeService.getEmpInfo(empId);
    }

    @PutMapping("update/personal/details")
    public String updatePersonalDetails(@RequestBody Employee employee){
        return employeeService.updatePersonalDetails(employee);
    }

    @PostMapping("mark/attendance")
    public String markAttendance(@RequestParam Long empId){
        return reportService.markAttendance(empId);
    }

}

package com.api.costing.controller;

import com.api.costing.service.DepartmentService;
import com.api.costing.ui.model.request.DepartmentRequestModel;
import com.api.costing.ui.model.response.DepartmentResponseModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/department")
public class DepartmentController {
	
	@Autowired
	DepartmentService departmentService;
	
	@PostMapping
	public DepartmentResponseModel saveDepartment(@RequestBody DepartmentRequestModel departmentDetail) {
		DepartmentResponseModel returnValue = departmentService.saveDepartment(departmentDetail);
		return returnValue;
	}
	
	@GetMapping(path = "/{departmentId}")
	public DepartmentResponseModel getDepartment(@PathVariable Integer departmentId) {
		DepartmentResponseModel returnValue = departmentService.getDepartment(departmentId);
		return returnValue;
	}
	
	@GetMapping
	public List<DepartmentResponseModel> getAllDepartments(@RequestParam(value="searchKey", defaultValue = "") String searchKey, @RequestParam(value="page", defaultValue = "1") int page,
			   @RequestParam(value="limit", defaultValue = "25") int limit){
		
		List<DepartmentResponseModel> returnValue = departmentService.getAllDepartments(page,limit, searchKey);
		
		return returnValue;
		
	}
	
	@PutMapping(path = "/{departmentId}")
	public DepartmentResponseModel updateDepartment(@PathVariable Integer departmentId, @RequestBody DepartmentRequestModel departmentDetail) {
		DepartmentResponseModel returnValue = departmentService.updateDepartment(departmentId,departmentDetail);
		return returnValue;
	}
	
	@DeleteMapping(path="/{departmentId}")
	public String deleteDepartment(@PathVariable Integer departmentId) {
		
		String returnValue = departmentService.deleteDepartment(departmentId);
		return returnValue;
	}

}

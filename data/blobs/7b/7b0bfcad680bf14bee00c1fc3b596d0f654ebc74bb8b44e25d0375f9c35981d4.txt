package com.Nimap.Test.Controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import com.Nimap.Test.Models.Categories;
import com.Nimap.Test.Services.CategoriesService;

@RestController
@RequestMapping("/api/categories")
public class CategoriesController {
	@Autowired
	CategoriesService catserv;

	
	//For Fetching all details with pagination
	@GetMapping
	public ResponseEntity<Page<Categories>> getAllCategories(@RequestParam(defaultValue = "0") int page,
			@RequestParam(defaultValue = "5") int size) {

		Page<Categories> categ = catserv.findAllCategories(page, size);

		return ResponseEntity.ok(categ);
	}

	
	//To Add New Category
	@PostMapping
	public String AddCategory(@RequestBody Categories c) {

		boolean b = catserv.saveCat(c);
		if (b) {
			return "Category Added Successfully";
		} else {
			return "some problem is there.....";
		}
	}

	
	//Find Category By Id
	@GetMapping(value = "/{cid}")
	public Categories findCatById(@PathVariable int cid) {

		Categories catid = catserv.getCatbyId(cid);

		if (catid != null) {
			return catid;
		} else {
			return null;
		}
	}
	
	
	//To Update Category By id
	@PutMapping("/{id}")
	public ResponseEntity<String>updateCatgoery(@PathVariable int id,@RequestBody Categories c)
	{
		boolean update=catserv.updateCategory(id, c);
		if(update)
		{
			return ResponseEntity.ok("Category updated successfully");
		}
		else
		{
			return ResponseEntity.status(404).body("Category not found");
		}
	}

	
	//To Delete Category By Id
	@DeleteMapping("/{cid}")
	public String DelById(@PathVariable int cid) {

		boolean b = catserv.DelCatById(cid);
		if (b) {
			return "Record \t" + cid + "\tdeleted Successfully.";
		} else {
			return "Some Problem is there...";
		}
	}
	
	

}

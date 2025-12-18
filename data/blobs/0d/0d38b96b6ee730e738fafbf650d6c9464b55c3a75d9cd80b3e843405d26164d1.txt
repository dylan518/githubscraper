package com.main.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.main.model.Product;
import com.main.proxy.ProductServiceProxy;

@RestController
public class ProductConsumerController {

	@Autowired
	private ProductServiceProxy productServiceProxy;
	
	@GetMapping("/getAllProducts")
	public List<Product> getAllProducts(){
		return productServiceProxy.getAllProducts();
	}
	
	@GetMapping("/getBookById/{id}")
	public Product getProductById(@PathVariable("id") int id) {
		Product product = productServiceProxy.getProductById(id);
		return product;
	}
	
	
	
	
	
}

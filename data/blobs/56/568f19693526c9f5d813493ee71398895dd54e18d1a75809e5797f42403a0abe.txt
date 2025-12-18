package com.ecommerce.ecommerce.api.controllers;


import com.ecommerce.ecommerce.business.abstracts.ProductService;
import com.ecommerce.ecommerce.core.utilities.results.DataResult;
import com.ecommerce.ecommerce.entities.concretes.Product;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("api/product")
public class ProductController {
    private ProductService productService;
@Autowired
    public ProductController(ProductService productService) {
        this.productService = productService;
    }
    @GetMapping("/")
    public DataResult<List<Product>> getAll(){
        return productService.getList();
    }
}

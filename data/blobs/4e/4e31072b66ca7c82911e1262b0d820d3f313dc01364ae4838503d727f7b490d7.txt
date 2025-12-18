package com.spring.l10springdetails.controllers;

import com.spring.l10springdetails.services.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/product")
public class ProductController {

    private final ProductService productService;

    @Autowired
    public ProductController(final ProductService productService){
        this.productService = productService;
    }

    @PostMapping("/addProduct/{name}")
    public void addProduct(@PathVariable String name){
        productService.addProduct(name);
    }

}

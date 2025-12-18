package com.example.Monster.Shop.controller;

import com.example.Monster.Shop.model.Product;
import com.example.Monster.Shop.repository.ProductRepository;
import com.example.Monster.Shop.service.ProductService;
import lombok.NoArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ProductController {
    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @GetMapping("/products")
    public List<Product> getAllProducts(){
        return productService.getAll();
    }

    @PostMapping("/products")
    public void createProduct(@RequestBody Product newProduct){
        productService.addProduct(newProduct);
    }

}

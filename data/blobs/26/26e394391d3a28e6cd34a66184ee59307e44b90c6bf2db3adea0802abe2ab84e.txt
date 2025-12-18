package com.ensat.controllers;

import com.ensat.DTO.ProductDTO;
import com.ensat.entities.Product;
import com.ensat.services.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

/**
 * Homepage controller.
 */
@RestController
public class ProductController {

    @Autowired
    private ProductService productService;

    @GetMapping("/")
    String index() {
        return "index";
    }

    @GetMapping("/getAllProduct")
    ResponseEntity<?> list() {
        return ResponseEntity.ok(productService.listAllProducts());
    }

    @GetMapping("/getProduct")
    public ResponseEntity<?> getProduct(@RequestParam String id) {
        return ResponseEntity.ok(productService.getProductById(Integer.valueOf(id)));
    }

    @PostMapping("/saveProduct")
    ResponseEntity<?> saveProduct(@RequestBody Product product) {
        productService.saveProduct(product);
        return ResponseEntity.ok(product);
    }

    @PostMapping("/updateProduct")
    public ResponseEntity<?> updateProduct(@RequestBody Product product) {
        productService.saveProduct(product);
        return ResponseEntity.ok(product);
    }

    @DeleteMapping("/deleteProduct")
    public ResponseEntity<?> deleteProduct(@RequestParam Integer id) {
        if (!productService.getProductById(id).isPresent()) {
            return ResponseEntity.ok("Product not found with id: " + id);
        }
        productService.deleteProduct(id);
        return ResponseEntity.ok("Product deleted successfully with id: " + id);
    }

}

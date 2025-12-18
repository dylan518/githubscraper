package com.example.springbootcrudexample1.service;

import com.example.springbootcrudexample1.entity.Product;
import com.example.springbootcrudexample1.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ProductService {
    @Autowired
    private ProductRepository repository;

    public Product saveProduct(Product product) {
        return repository.save(product);
    }

    public List<Product> saveProducts(List<Product> products) {
        return repository.saveAll(products);
    }

    public Product findProductById(int id) {
        return repository.findById(id).orElse(null);
    }

    public Product findProductByName(String name) {
        return repository.findByName(name);
    }

    public List<Product> getAllProducts() {
        return repository.findAll();
    }

    public String deleteProduct(int id) {
        repository.deleteById(id);
        return "Product Deleted ||" + id;
    }

    public Product updateProduct(Product product) {
        Product existingProduct = findProductById(product.getId());
        existingProduct.setName(product.getName());
        existingProduct.setPrice(product.getPrice());
        existingProduct.setQuantity(product.getQuantity());
        return existingProduct;
    }
}

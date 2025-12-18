package com.ademozalp.hibernate.service;


import com.ademozalp.hibernate.dto.CountByName;
import com.ademozalp.hibernate.model.Detail;
import com.ademozalp.hibernate.model.Product;
import com.ademozalp.hibernate.model.Test;
import com.ademozalp.hibernate.repository.ProductRepository;
import com.ademozalp.hibernate.repository.TestRepository;
import com.github.javafaker.Faker;
import jakarta.annotation.PostConstruct;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityNotFoundException;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.retry.annotation.Backoff;
import org.springframework.retry.annotation.Recover;
import org.springframework.retry.annotation.Retryable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

@Service
@Slf4j
@RequiredArgsConstructor
public class ProductService {
    private final ProductRepository repository;
    private final EntityManager entityManager;
    private final TestRepository testRepository;
    private final ProductRepository productRepository;


    @PostConstruct
    @Transactional
    public void initialize() {
        Faker faker = new Faker();

        List<Product> products = new ArrayList<>();
        for (int i = 0; i < 100; i++) {
            Product product = Product.builder()
                    .price(BigDecimal.valueOf(faker.number().randomDouble(2, 10, 1000)))
                    .stock(faker.number().numberBetween(1, 100))
                    .detail(new Detail(faker.commerce().productName(), faker.lorem().sentence()))
                    .build();
            products.add(product);
        }
        productRepository.saveAll(products);

        List<CountByName> countGroupedByName = productRepository.getCountGroupedByName();
        for (CountByName countByName : countGroupedByName) {
            System.out.println(countByName.toString());
        }
    }

    public void save(Product product) {
        repository.save(product);
    }

    @Transactional
    @Cacheable(cacheNames = "getAllProducts")
    public List<Product> getAllProducts() {
        try {
//            Thread.sleep(5000L);
            return repository.findAll();
        } catch (Exception e) {
            throw new RuntimeException(e.getMessage());
        }
    }

    @Transactional
    @Retryable(retryFor = RuntimeException.class, maxAttempts = 2, backoff = @Backoff(delay = 1000))
    public Product incrementStock() {
        Product product = repository.findAll().getFirst();

        product.setStock(product.getStock() + 1);
        return repository.save(product);

//        return retryTemplate.execute(context -> hataVerecekMethod());
    }

    @Recover
    public Product recover(RuntimeException e, Product product) throws Throwable {
        log.info("2 denemeden sonra buraya dustu: {}", e.getMessage());

        return product;
    }

    public List<Test> getAllTests() {
        return testRepository.findAll();
    }

//    public Product hataVerecekMethod() {
//        Product product = repository.findByDetailName("Laptop")
//                .orElseThrow(() -> new EntityNotFoundException("Product not found: Laptop"));
//
//        product.setStock(product.getStock() + 1);
//        return repository.save(product);
//    }
}

package org.piolig.java.jdbc.service;

import org.piolig.java.jdbc.model.Category;
import org.piolig.java.jdbc.model.Product;
import org.piolig.java.jdbc.repository.CategoryRepositoryImpl;
import org.piolig.java.jdbc.repository.ProductRepository;
import org.piolig.java.jdbc.repository.Repository;
import org.piolig.java.jdbc.util.DBConnection;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;

public class CatalogService implements Service {


    private Repository<Product> productRepository;
    private Repository<Category> categoryRepository;

    public CatalogService() {
        this.productRepository = new ProductRepository();
        this.categoryRepository = new CategoryRepositoryImpl();
    }

    @Override
    public List<Product> findAll() throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            productRepository.setConn(conn);
            return productRepository.findAll();
        }

    }

    @Override
    public Product byId(Long id) throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            productRepository.setConn(conn);
            return productRepository.byId(id);
        }

    }

    @Override
    public Product save(Product product) throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            productRepository.setConn(conn);
            if (conn.getAutoCommit()) {
                conn.setAutoCommit(false);
            }

            Product newProduct = null;
            try {
                newProduct = productRepository.save(product);
                conn.commit();
            } catch (SQLException e) {
                conn.rollback();
                e.printStackTrace();
            }
            return newProduct;
        }

    }

    @Override
    public void delete(Long id) throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            productRepository.setConn(conn);
            if (conn.getAutoCommit()) {
                conn.setAutoCommit(false);
            }

            try {
                productRepository.delete(id);
                conn.commit();
            } catch (SQLException e) {
                conn.rollback();
                e.printStackTrace();
            }
        }

    }

    @Override
    public List<Category> listCategory() throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            categoryRepository.setConn(conn);
            return categoryRepository.findAll();
        }
    }

    @Override
    public Category byIdCategory(Long id) throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            categoryRepository.setConn(conn);
            return categoryRepository.byId(id);
        }
    }

    @Override
    public Category saveCategory(Category category) throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            categoryRepository.setConn(conn);
            if (conn.getAutoCommit()) {
                conn.setAutoCommit(false);
            }

            Category newCategory = null;
            try {
                categoryRepository.save(category);
                conn.commit();
            } catch (SQLException e) {
                conn.rollback();
                e.printStackTrace();
            }
            return newCategory;
        }
    }

    @Override
    public void deleteCategory(Long id) throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            categoryRepository.setConn(conn);

            if (conn.getAutoCommit()) {
                conn.setAutoCommit(false);
            }

            try {
                conn.commit();
            } catch (SQLException e) {
                conn.rollback();
                e.printStackTrace();
            }
        }

    }

    @Override
    public void saveProductWithCategory(Product product, Category category) throws SQLException {
        try (Connection conn = DBConnection.getConnection()) {
            productRepository.setConn(conn);
            categoryRepository.setConn(conn);

            if (conn.getAutoCommit()) {
                conn.setAutoCommit(false);
            }

            try {
                Category newCategory = categoryRepository.save(category);
                product.setCategory(newCategory);
                productRepository.save(product);
                conn.commit();
            } catch (SQLException e) {
                conn.rollback();
                e.printStackTrace();
            }
        }

    }
}
